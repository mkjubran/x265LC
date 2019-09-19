# x265LC

# Learnable Coding

## Introduction

This repository contains our public tools for .... 

## Prerequisites

In order to compile and run the tools provided in this repository you will need:
1. Python 2.7 
2. ffmpeg (version 2.8.15 or higher)

## To produce data for training the network
To extract the informartion needed to prepare the training data, run an ffmpeg comand with the libx265 (modified) similar to:

```
../ffmpeg/ffmpeg -y -i ../../vid/park_joy_640480.mp4 -vcodec libx265 -crf 12 -pass 1 -an -f mp4 /dev/null
```

Noew, to produce the necessary data to train the network run:

```
python python ./Produce_x265_InfoPerFrame.py --file_video=../../vid/park_joy_640480.mp4 --file_perframe=x265LC_InfoPerFrame.txt --path=../x265LC_Results
```

Option | Description [default]
---|---
--file_video | input file name 
--file_perframe | text file contains rate, type, and RPS per frame [x265LC_InfoPerFrame.txt]
--path | path for results [../HMLC_Results]

A successful run will produce the following:
- a binary file with number of bits required to encode each picture 
- a folder contains the encoded pictures; Px.jpg is the fifth encoded picture
- a folder contains all inter-prediction pictures; Px_y.jpg is the reference picture y used for inter-prediction of picture x

