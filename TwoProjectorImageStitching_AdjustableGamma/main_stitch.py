#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from config_reader import Config_Reader
from image_correction import Image_Correction
import numpy as np
import cv2
# ˄

CR = Config_Reader()
IC = Image_Correction()

class Main_Stitch(object):

    def __init__(self):
        # ˅
        pass
        # ˄

    def displayImage():
        # ˅
        gamma = float(CR.getGamma())
        img = IC.alphaBlending(gamma)
        frame = 0
        
        while 1:
            frame += 1
            
            imgtxt = img.copy()
            #imgtxt = cv2.putText(imgtxt, "Current Gamma:" + str(round(gamma,2)) + ", Frame:" + str(frame), org = (640, 700), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (0,0,255))
            cv2.imshow("", imgtxt)
            
            key = cv2.waitKey(1)
            if key == 27:
                break
            elif key == ord('w'):
                gamma += 0.1
                img = IC.alphaBlending(gamma)
            elif key == ord('s'):
                if gamma - 0.1 > 0:
                    gamma -= 0.1
                    img = IC.alphaBlending(gamma)
            elif key == ord('e'):
                gamma += 0.01
                img = IC.alphaBlending(gamma)
            elif key == ord('d'):
                if gamma - 0.01 > 0:
                    gamma -= 0.01
                    img = IC.alphaBlending(gamma)
        cv2.destroyAllWindows()
        # ˄

    displayImage()
