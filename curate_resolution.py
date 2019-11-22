import os, sys, subprocess
import pdb
import re
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

#identify -format "%[fx:w]x%[fx:h]"

# Optional argument

parser.add_argument('--w', type=int,
                    help='Original Width')

parser.add_argument('--h', type=int,
                    help='Original Hight')

parser.add_argument('--rps', type=int,
                    help='RPS length; n=0 Intra-prediction, n=1 one predictor')

parser.add_argument('--in_dir', type=str,
                    help='Input Directory')

parser.add_argument('--override', type=str,
                    help='Override training data [y/Y or n/N]')


args = parser.parse_args()
width=args.w;
hight=args.h;
rps=args.rps;
input_dir=args.in_dir;
override=args.override;

# Code for pre processing:
# ffmpeg -i sintel.mp4  -crf 16 -bf 0 sintel_2.mp4

def call(cmd):
   #print(cmd)
   return subprocess.check_output(cmd, shell=True)


# Prepare output dir ..
if (( override == 'Y') or (override == 'y')):
    cmd = 'rm -rf {}_curated'.format(input_dir) ; output = call(cmd)

if not os.path.exists('{}_curated'.format(input_dir)):
    os.makedirs('{}_curated'.format(input_dir))

if not os.path.exists('{}_BadResolution'.format(input_dir)):
    os.makedirs('{}_BadResolution'.format(input_dir))

#cmd = 'mkdir  {}'.format(out_dir) ; output = call(cmd)
cmd = 'ls {}/ | wc -l'.format(input_dir); output = call(cmd); print('Original pngs are {}'.format(output));
for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
       cmd = 'identify -format "%[fx:w]x%[fx:h]" {}/{}'.format(input_dir,filename)
       Res = call(cmd); W=int(Res.split('x')[0]);H=int(Res.split('x')[1]);
       #print('{}x{}'.format(W,H))
       if (rps == 0):
         #pdb.set_trace()
         if (W == 2*width) and (H == hight):
           cmd = 'cp -rf {}/{} {}_curated/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
         else:
           cmd = 'cp -rf {}/{} {}_BadResolution/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
       elif (rps == 1):
         if (W == 3*width) and (H == hight):
           cmd = 'cp -rf {}/{} {}_curated/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
         else:
           cmd = 'cp -rf {}/{} {}_BadResolution/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
       elif (rps == 2):
         if (W == 4*width) and (H == hight):
           cmd = 'cp -rf {}/{} {}_curated/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
         else:
           cmd = 'cp -rf {}/{} {}_BadResolution/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
       elif (rps == 4):
         if (W == 6*width) and (H == hight):
           cmd = 'cp -rf {}/{} {}_curated/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
         else:
           cmd = 'cp -rf {}/{} {}_BadResolution/.'.format(input_dir,filename,input_dir) ; 
           output = call(cmd)
       else:
          print('There is no curration for the  input rps of {}'.format(rps))


#cmd = 'ls {}/ | wc -l'.format(input_dir); output = call(cmd); print('Original pngs are {}'.format(output));
cmd = 'ls {}_curated/ | wc -l'.format(input_dir); output = call(cmd); print('Curated pngs are {}'.format(output));
cmd = 'ls {}_BadResolution/ | wc -l'.format(input_dir); output = call(cmd); print('Bad Resolution pngs are {}'.format(output));

