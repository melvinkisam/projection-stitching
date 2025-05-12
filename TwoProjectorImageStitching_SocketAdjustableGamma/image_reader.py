#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config_reader import Config_Reader
import cv2

class Image_Reader(object):

    def __init__(self):
        pass

    def getImage(self):
        imagePath = []      
        CR = Config_Reader()

        imageLeft = cv2.imread(CR.getImageLeftPath())
        #imageLeft = cv2.cvtColor(imageLeft, cv2.COLOR_RGB2RGBA)

        imagePath.append(imageLeft)

        imageRight = cv2.imread(CR.getImageRightPath())
        #imageRight = cv2.cvtColor(imageRight, cv2.COLOR_RGB2RGBA)

        imagePath.append(imageRight)

        return imagePath
