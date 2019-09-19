# x265LC

# Learnable Coding

## Introduction

This repository contains our public tools for .... 

## Prerequisites

In order to compile and run the tools provided in this repository you will need Python 2.7

## Compilation & Installation

Use the instruction provided in http://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu to compile and install libx265 and ffmpeg. To compile libx265, use the modified source files provided in this repository.

## Neural Network Training Data
To extract the information needed to prepare the training data, run an ffmpeg command with the modified libx265 similar to:

```
./ffmpeg -y -i ../../vid/park_joy_640480.mp4 -vcodec libx265 -crf 12 -pass 1 -an -f mp4 /dev/null
```

Now, to produce the necessary data to train the neural network run:

```
python python ./Produce_x265_InfoPerFrame.py --file_video=../../vid/park_joy_640480.mp4 --file_perframe=x265LC_InfoPerFrame.txt --path=../x265LC_Results
```

Option | Description [default]
---|---
--file_video | input file name 
--file_perframe | text file contains rate, type, and RPS per frame [x265LC_InfoPerFrame.txt]
--path | path for results [../x265LC_Results]

A successful run will produce the following:
- a binary file with number of bits required to encode each picture 
- a folder contains the encoded pictures; Px.jpg is the fifth encoded picture
- a folder contains all inter-prediction pictures; Px_y.jpg is the reference picture y used for inter-prediction of picture x
