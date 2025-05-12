#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config_reader import Config_Reader
from image_correction import Image_Correction
from PIL import Image
import socket
import cv2

CR = Config_Reader()
IC = Image_Correction()

class Main_Stitch(object):
    frame = 0
    def __init__(self):
        pass

    def sendImage(self):
        if(CR.getProjectorSide() == "left" ):       
            sendImage = open("OutputRight.png", "rb")
            
        elif(CR.getProjectorSide() == "right"):
            sendImage = open("OutputLeft.png", "rb")

        s = socket.socket()
        s.connect(("192.168.0.121", 8888))
        
        for i in sendImage:
            s.send(i)
    
    def displayImage(self):
        texttimeout = 100
        textcounter = 0
        gamma = CR.getGamma()
        while True:
            self.frame +=1
            outputImages = IC.alphaBlending(gamma)
            
            if(CR.getProjectorSide() == "left"):
                if textcounter < texttimeout:
                    outtext = outputImages[0].copy()
                    cv2.imshow("OutputLeft.png", cv2.putText(outtext, "Current Gamma:" + str(round(gamma,2)) + ", Frame:" + str(self.frame)+" Save with (Q)", org = (400, 700), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (0,0,255)))
                else:
                    cv2.imshow("OutputLeft.png", outputImages[0])
            elif(CR.getProjectorSide() == "right"):
                if textcounter < texttimeout:
                    outtext = outputImages[1].copy()
                    cv2.imshow("OutputRight.png", cv2.putText(outtext, "Current Gamma:" + str(round(gamma,2)) + ", Frame:" + str(self.frame)+" Save with (Q)", org = (400, 700), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (0,0,255)))
                else:
                    cv2.imshow("OutputRight.png", outputImages[1])
                
            
            key = cv2.waitKey(1)
            if key == 27:
                break
            if key == ord('q'):
                CR.setGammaSetting(str(round(gamma,2)))
            else:
                if key == ord('w') or key == ord('s') or key == ord('e') or key == ord('d') or self.frame == 1:
                    textcounter = 0
                    if key == ord('w'):
                        gamma += 0.1
                        
                    elif key == ord('s'):
                        if gamma - 0.1 > 0:
                            gamma -= 0.1
                    elif key == ord('e'):
                        gamma += 0.01
                        
                    elif key == ord('d'):
                        if gamma - 0.1 > 0:
                            gamma -= 0.01
                    outputImages = IC.alphaBlending(gamma)
                    self.sendImage()
            textcounter+=1
                
        cv2.destroyAllWindows()
        
Main_Stitch().displayImage()


