# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:52:22 2021

@author: quinj
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

class ROI():
    def __init__(self):
        print("ROI Class Initialized")
    
    def Process(self, image):
        h, w = image.shape
        img = np.zeros((h+160,w), np.uint8)
        img[80:-80,:] = image
        blur = cv2.GaussianBlur(img,(5,5),0)
        _, th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        print(cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        print(image.shape)
        
        M = cv2.moments(th)
        h, w = img.shape
        x_c = M['m10'] // M['m00']
        y_c = M['m01'] // M['m00']
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]]).astype(np.uint8)
        erosion = cv2.erode(th,kernel,iterations=1)
        boundary = th-erosion
        
        cnt, _ = cv2.findContours(boundary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        img_c = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cnt = cnt[0]
        img_cnt = cv2.drawContours(img_c, [cnt], 0, (255,0,0), 2)
        
        cnt = cnt.reshape(-1,2)
        left_id = np.argmin(cnt.sum(-1))
        cnt = np.concatenate([cnt[left_id:,:], cnt[:left_id,:]])
        
        dist_c = np.sqrt(np.square(cnt-[x_c, y_c]).sum(-1))
        f = np.fft.rfft(dist_c)
        cutoff = 15
        f_new = np.concatenate([f[:cutoff],0*f[cutoff:]])
        dist_c_1 = np.fft.irfft(f_new)
        
        eta = np.square(np.abs(f_new)).sum()/np.square(np.abs(f)).sum()
        print('Power Retained: {:.4f}{}'.format(eta*100,'%'))
        
        derivative = np.diff(dist_c_1)
        sign_change = np.diff(np.sign(derivative))/2
        
        minimas = cnt[np.where(sign_change>0)[0]]
        v1, v2 = minimas[-2], minimas[-4]
        
        theta = np.arctan2((v2-v1)[1], (v2-v1)[0])*180/np.pi
        print('The rotation of ROI is {:.02f}\u00b0'.format(theta))
        R = cv2.getRotationMatrix2D(tuple(v2),theta,1)
        img_r = cv2.warpAffine(img,R,(w,h))
        v1 = (R[:,:2] @ v1 + R[:,-1]).astype(np.int)
        v2 = (R[:,:2] @ v2 + R[:,-1]).astype(np.int)
        
        ux = v1[0]
        uy = v1[1] + (v2-v1)[0]//3
        lx = v2[0]
        ly = v2[1] + 4*(v2-v1)[0]//3
        img_c = cv2.cvtColor(img_r, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(img_c, (lx,ly),(ux,uy),(0,255,0),2)
        
        roi = img_r[uy:ly,ux:lx]
        
        return roi