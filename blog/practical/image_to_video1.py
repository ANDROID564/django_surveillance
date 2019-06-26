# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:19:22 2019

@author: TANVEER_MUSTAFA
"""

import cv2
import numpy as np
import os
 
from os.path import isfile, join
 
class video_converter:
    
    def main(directory=os.getcwd()):
        print(directory)
        pathIn= directory
        pathOut = 'video.avi'
        #print('pathOut',pathOut)
        fps = 25.0
        
        frame_array = []
        files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
     
        #for sorting the file names properly
        files.sort(key = lambda x: int(x[5:-4]))
     
        for i in range(len(files)):
            filename=pathIn + files[i]
            #reading each files
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            print(filename)
            #inserting the frames into an image array
            frame_array.append(img)
     
        out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
     
        for i in range(len(frame_array)):
            # writing to a image array
            out.write(frame_array[i])
        return pathOut
        out.release()


        
       