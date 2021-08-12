#!/bin/bash

# $1 is the filename without py, $2 is the Scene class name

python3 -m manim $1.py $2
if [ $? -eq 0 ]
then
   ffmpeg -y -i media/videos/$1/1080p60/$2.mp4 -r 15 media/videos/$1/1080p60/$2.gif
fi

