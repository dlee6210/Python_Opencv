# -*- coding:utf-8 -*-
'''
通过opencv内部的VideoCapture读取文件,通过自带的HaarLink进行人脸识别
获取摄像头输入失败
'''
import cv2 as cv

cap = cv.VideoCapture('C:\quanwei\BMP\qqzb.wmv')#input('InputPath=:')

#cap = cv.VideoCapture(0)

cv.namedWindow('frame')

if cap.isOpened() == False:
    print('Open Failed')

minisize = (5, 5)

while(True):
    ret,frame = cap.read()
    if ret == True:

        gray = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)

        face_cascade = cv.CascadeClassifier('C:\Program Files\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

        faces = face_cascade.detectMultiScale(gray,
                                              1.15,
                                              5,
                                              cv.CASCADE_SCALE_IMAGE,
                                              minisize
                                              )
        for(x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+w),(0,0,255),2 )

        cv.imshow('frame',frame)

    if cv.waitKey(1) == ord('q'):
        break