#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from config_reader import Config_Reader
from image_reader import Image_Reader
import cv2
import numpy as np
# ˄


CR = Config_Reader()
IR = Image_Reader()

class Image_Correction(object):
    currentgamma = 0
    image = IR.getImage()
    imageHeight = image.shape[0]
    imageWidth = image.shape[1]
    imageChannel = image.shape[2]
    maskSize = int(CR.getmaskLengthCm() / CR.getimageWidthCm() * CR.getimageWidthPx())
    gammamask = []

    def __init__(self):
        # ˅
        pass
        # ˄

    def alphaBlending(self,gamma):
        # ˅
        '''
        print("Image height: " + str(self.imageHeight) + " px")
        print("Image width: " + str(self.imageWidth) + " px")
        print("Image Channels: " + str(self.imageChannel))
        '''
        if gamma != self.currentgamma or gamma == 0:
            self.image = IR.getImage()
            print("New Gamma: " + str(gamma))
            self.currentgamma = gamma
            self.gammamask = []
            for i in range(self.maskSize):
                
                if(CR.getProjectorSide().lower() == "right"):
                    gammav = self.gammaCorrection(i, self.maskSize, gamma)
                else:
                    gammav = self.gammaCorrection((self.maskSize - i), self.maskSize, gamma)
                self.gammamask.append(gammav)
        

        
        for i in range(self.maskSize):
            for j in range(self.imageHeight):
                if(CR.getProjectorSide().lower() == "right"):
                    self.image[j][i] = self.image[j][i]*(self.gammamask[i]/255) 
                else:
                    self.image[j][i + self.imageWidth - self.maskSize] = self.image[j][i + self.imageWidth - self.maskSize]*(self.gammamask[i]/255) 

        
        
        output = cv2.cvtColor(self.image, cv2.COLOR_RGBA2RGB)
        cv2.imwrite("Output.png", output)
        
        return self.image
        # ˄

    def gammaCorrection(self, x, px, gamma):
        # ˅
        powerLaw = pow((x / px), gamma) * 255

        return powerLaw
        # ˄
