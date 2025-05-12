#!/usr/bin/env python
# -*- coding: utf-8 -*-
from configparser import ConfigParser

class Config_Reader(object):

    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")

        for settings in config.sections():
            self.imageLeftPath = config.get(settings, "imageLeftPath")
            self.imageRightPath = config.get(settings, "imageRightPath")
            self.projectorSide = config.get(settings, "projectorSide")
            self.gamma = config.get(settings, "gamma")
            self.imageWidthCm = config.get(settings, "imageWidthCm")
            self.imageWidthPx = config.get(settings, "imageWidthPx")
            self.maskLengthCm = config.get(settings, "maskLengthCm")      

    def getProjectorSide(self):
        return self.projectorSide

    def getImageLeftPath(self):
        return self.imageLeftPath

    def getImageRightPath(self):
        return self.imageRightPath

    def getGamma(self):
        return float(self.gamma)

    def getimageWidthCm(self):
        return int(self.imageWidthCm)

    def getimageWidthPx(self):
        return int(self.imageWidthPx)

    def getmaskLengthCm(self):
        return int(self.maskLengthCm)
    
    def setGammaSetting(self, gamma):
        config = ConfigParser()
        config.read("config.ini")
        config.set('settings','gamma',str(gamma))
        with open('config.ini','w') as configfile:
            config.write(configfile)
        print("Gamma of "+str(gamma)+" saved to config.ini")
        
