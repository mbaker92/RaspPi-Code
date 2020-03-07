#!/bin/bash
raspivid -vf -o original.h264 -t "$(($1*1000))" 
MP4Box -add original.h264 "$(date)".mp4
rm original.h264
