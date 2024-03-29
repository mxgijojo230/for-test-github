# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:39:00 2019

@author: Darren
"""

import cv2


#載入分類器
face_case=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#讀取攝影鏡頭
cap=cv2.VideoCapture(0)

#或者讀取影片檔案
#cap=cv2.VideoCapture('filename.mp4')

if cap.isOpened()==0:
   print("error")
   
while True:
    #read the Frame

    frame=cap.read()
    #frame[0] 由於cap.read()第一陣列為布林函數用來判斷攝影機好壞
    if(frame[0] == False):
        print("check device")
        break
    #gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    cv2.imshow('img',frame[1])
    #stopkey
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

#解除所有攝影機    
cap.release()
#關閉所有opencv 視窗
cv2.destroyAllWindows()
    
    