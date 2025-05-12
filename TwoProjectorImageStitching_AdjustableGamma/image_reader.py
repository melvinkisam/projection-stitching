#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import cv2
import numpy
from config_reader import Config_Reader

# ˄

class Image_Reader(object):

    def __init__(self):
        # ˅
        pass
        # ˄

    def getImage(self):
        # ˅
        CR = Config_Reader()
        image = cv2.imread(CR.getImagePath())
        image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
        
        return image
        # ˄
    getImage(0)