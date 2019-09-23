from __future__ import division
import numpy as np
import os, sys, subprocess, pdb
import argparse, re
import matplotlib.pyplot as plt
import datetime, math, time
import pickle
from array import *

###--------------------------------------------------------------
# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Optional argument
parser.add_argument('--file_video',nargs='?',default ='../../vid/park_joy_640480.mp4', type=str, help='file name [mp4]')
parser.add_argument('--file_perframe',nargs='?',default ='./x265LC_InfoPerFrame.txt', type=str, help='file name [txt]')
parser.add_argument('--path',nargs='?',default ='../HMLC_Results/', type=str, help='path for results [../x265LC_Results]')
args = parser.parse_args()

###--------------------------------------------------------------
def call(cmd):
    # proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
    proc = subprocess.Popen(cmd, shell=True)
    #proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return (out, err)

###--------------------------------------------------------------
def call_bg(cmd):
    #proc = subprocess.Popen(cmd, shell=True)
    proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    return proc

###--------------------------------------------------------------
def export_frames(fn):
    osout = call('ffmpeg -r 1 -i {} -r 1 {}/POC/%d.jpg'.format(fn,video_path))
    return 

###--------------------------------------------------------------
def produce_training_data(finfo):
    with open(finfo) as fi:
       lines = fi.readlines()
    Bits=[]
    for cnt in range(len(lines)):
       line = re.sub(' +', ' ', lines[cnt]).lstrip().split(' ')
       POC = line[0]
       POCtype = line[1]
       #print(POCtype);
       #pdb.set_trace();
       Frame = str(int(line[0])+1) ## Frame=POC+1
       osout = call('cp -rf {} {}'.format(video_path+'/POC/'+Frame+'.jpg',video_path+'/x265LCPOC/P'+POC+'.jpg'))
       Bits.append(int(line[2]))
       L0 = re.sub(' +', ' ', lines[cnt]).split('L0')[1].split(' ')[1:-1]
       L1 = re.sub(' +', ' ', lines[cnt]).split('L1')[1].split(' ')[1:-1]

       L0 = list(set(L0));
       L1 = list(set(L1));

       L0 = [ elem for elem in L0 if elem != '-1' ]
       L1 = [ elem for elem in L1 if elem != '-1' ]
       #pdb.set_trace()
       if (POCtype == 'P'):
          for cnt2 in range(len(L0)):
             L0Frame= str(int(L0[cnt2])+1)
             L0POC=L0[cnt2]
             osout = call('cp -rf {} {}'.format(video_path+'/POC/'+L0Frame+'.jpg',video_path+'/x265LCPOC/P'+POC+'_L0_'+L0POC+'.jpg'))

       if (POCtype == 'B'):
          for cnt2 in range(len(L0)):
             L0Frame= str(int(L0[cnt2])+1)
             L0POC=L0[cnt2]
             osout = call('cp -rf {} {}'.format(video_path+'/POC/'+L0Frame+'.jpg',video_path+'/x265LCPOC/P'+POC+'_L0_'+L0POC+'.jpg'))
          for cnt2 in range(len(L1)):
             L1Frame= str(int(L1[cnt2])+1)
             L1POC=L1[cnt2]
             osout = call('cp -rf {} {}'.format(video_path+'/POC/'+L1Frame+'.jpg',video_path+'/x265LCPOC/P'+POC+'_L1_'+L1POC+'.jpg'))

    fb = open(video_path+'/x265LCPOC/rate.bin','wb')
    pickle.dump(Bits,fb)
    fb.close()
#    print(Bits)
#    fb = open(video_path+'/HMLCPOC/rate.bin','rb')
#    Bitsnew=pickle.load(fb)
#    print(Bitsnew)
    return

###--------------------------------------------------------------
if __name__ == '__main__':

 file_video=args.file_video;
 file_perframe=args.file_perframe;
 #qp=args.qp;
 #mcu=args.mcu;
 #mpd=args.mpd;
 #nf=args.nf;
 #fps=args.fps
 path=args.path;
 #w=args.w;
 #h=args.h;
 #rate=args.rate;
 #cfg=args.cfg;

 vid=file_video.split('/')[-1]
 video_path=path+vid[:-4]+'/'
 
 if (not os.path.isdir(path[:-1])):
    osout = call('mkdir {}'.format(path[:-1]))

 if (os.path.isdir(video_path[:-1])):
    osout = call('rm -rf {}'.format(video_path[:-1]))

 osout = call('mkdir {}'.format(video_path[:-1]))
 osout = call('rm -rf {}'.format(video_path+'/POC'))
 osout = call('mkdir {}'.format(video_path+'/POC'))
 osout = call('rm -rf {}'.format(video_path+'/x265LCPOC'))
 osout = call('mkdir {}'.format(video_path+'/x265LCPOC'))

 export_frames(file_video);
 produce_training_data(file_perframe);
