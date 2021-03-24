# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:52:11 2021

@author: swapnil pandit
"""

import cv2
import numpy as np
from time import sleep

width = 40
height =40
Threshold=2
position = 400

delay=60

detector=[]
vehicle=0

def model(x, y, w, h):
    x1=int(w / 2)
    y1=int(h / 2)
    a= x + x1 
    b= y + y1
    return a, b

#inp ={
#    'first' : '1615363610851.mp4',
#    'second' : '20201230123300.mp4',
#    'third' : 'Night Time Traffic Camera video.mp4',   
#}

# take user input
#print (input('enter which video you want check '))
cap= cv2.VideoCapture('Train Data/20201230123300.mp4')
subtractor= cv2.createBackgroundSubtractorMOG2()

while True:
    ret , frame1 = cap.read()
    temp=float(1/delay)
    sleep(temp)
    gray=cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray, (3, 3), 5)
    img=subtractor.apply(blur)
    dilated=cv2.dilate(img, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dil=cv2.morphologyEx (dilated, cv2.MORPH_CLOSE , kernel)
    dil1 = cv2.morphologyEx (dil, cv2.MORPH_CLOSE , kernel)
    Contours,h=cv2.findContours(dil1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, position), (1200, position), (255,127,0), 3) 
    for(i,c) in enumerate(Contours):
        (x,y,w,h) = cv2.boundingRect(c)
        Contours1 = (w >= width) and (h >= height)
        if not Contours1:
            continue
       
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
        center = model(x, y, w, h)
        detector.append(center)
        cv2.circle(frame1, center, 4, (0, 0,255), -1)
        
        for (x,y) in detector:
            if y<(position + Threshold) and y>(position - Threshold):
                vehicle+=1
                cv2.line(frame1, (25, position), (1200, position), (0,127,255), 3)  
                detector.remove((x,y))
                print("count is: "+str(vehicle))
                
    cv2.putText(frame1, "VEHICLE COUNT : "+str(vehicle), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
    cv2.imshow("Video Original" , frame1)
    cv2.imshow("Detectar",dil1)
    
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()




    
