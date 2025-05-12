#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config_reader import Config_Reader
from image_reader import Image_Reader
import cv2
import numpy as np

CR = Config_Reader()
IR = Image_Reader()

class Image_Correction(object):
    imageList = IR.getImage()
    imageLeft = imageList[0]
    imageRight = imageList[1]

    currentgamma = 0
    imageHeight = imageLeft.shape[0]
    imageWidth = imageLeft.shape[1]
    imageChannel = imageLeft.shape[2]
    maskSize = int(CR.getmaskLengthCm() / CR.getimageWidthCm() * CR.getimageWidthPx())
        
    def __init__(self):
        pass

    def gammaCorrection(self, maskSize, gamma):
        arr = np.empty((0,self.maskSize), float)
        for i in range(self.maskSize):
                arr = np.append(arr,pow(i/self.maskSize,gamma))
        return arr

    def alphaBlending(self, gamma):  

        if self.currentgamma != gamma or self.currentgamma == 0:
            self.currentgamma = gamma
            mask = self.gammaCorrection(self.maskSize, gamma)
            
        
            floatimageLeft = self.imageLeft.astype(float)
            floatimageRight = self.imageRight.astype(float)

            for i in range(self.maskSize):
                floatimageRight[:,i] *= mask[i]
                floatimageLeft[:,self.imageWidth-i-1] *= mask[i]
            
            OutputLeft = floatimageLeft.astype(np.uint8)
            OutputRight= floatimageRight.astype(np.uint8)

            cv2.imwrite("OutputLeft.png", OutputLeft)
            cv2.imwrite("OutputRight.png", OutputRight)

            self.imageList[0] = OutputLeft
            self.imageList[1] = OutputRight

        return self.imageList

    
