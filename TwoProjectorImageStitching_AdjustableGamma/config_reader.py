#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from configparser import ConfigParser
# ˄

class Config_Reader(object):

    def __init__(self):
        # ˅
        config = ConfigParser()
        config.read("config.ini")

        for settings in config.sections():
            self.imagePath = config.get(settings, "imagePath")
            self.projectorSide = config.get(settings, "projectorSide")
            self.gamma = config.get(settings, "gamma")  
            self.imageWidthCm = config.get(settings, "imageWidthCm")
            self.imageWidthPx = config.get(settings, "imageWidthPx")
            self.maskLengthCm = config.get(settings, "maskLengthCm")       
        # ˄

    def getImagePath(self):
        # ˅
        return self.imagePath
        # ˄

    def getProjectorSide(self):
        # ˅
        return self.projectorSide
        # ˄

    def getGamma(self):
        # ˅
        return self.gamma
        # ˄
    def getimageWidthCm(self):
        # ˅
        return float(self.imageWidthCm)
        # ˄

    def getimageWidthPx(self):
        # ˅
        return float(self.imageWidthPx)
        # ˄

    def getmaskLengthCm(self):
        # ˅
        return float(self.maskLengthCm)
        # ˄
