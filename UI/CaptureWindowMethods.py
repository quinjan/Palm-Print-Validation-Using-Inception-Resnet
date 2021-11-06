# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:39:41 2021

@author: quinj
"""

import os
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.CaptureWindow import Ui_CaptureWindow
from Common.DatasetGenerator import DatasetGenerator

class CaptureWindow(QtWidgets.QMainWindow, Ui_CaptureWindow):
    
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CaptureWindow, self).__init__(parent)
        self.setupUi(self)
           
        self.statusBar().showMessage('Ready')
        self.returnPushButton.clicked.connect(self.ReturnClicked)
        self.capturePushButton.clicked.connect(self.capture_image)
        
        self.imageLabel.setScaledContents(True)
        self.capture = None
        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 0
    
    @QtCore.pyqtSlot()
    def start_webcam(self):
        print("Initializing Camera")
        if self.capture is None:
            self.capture =cv2.VideoCapture(0 + cv2.CAP_DSHOW)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.timer.start()
        self.dsGen = DatasetGenerator(self.selectedMethod , self.userName)
        self.dsGen.InitializeDatasetFolder()
        self.usernameLabel.setText(self.userName + " " + str(self._image_counter))
    
    def destroy_webcam(self):
        print("Destroying Camera")
        if self.capture != None:
            self.timer.stop()
            self.capture.release()
            self.capture = None
    
    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, image=self.capture.read()
        image = cv2.flip(image, 1)
        self.displayImage(image, True)
        
    @QtCore.pyqtSlot()
    def capture_image(self):
        flag, frame= self.capture.read()
        if flag:
            QtWidgets.QApplication.beep()
            name = "{}.png".format(self._image_counter)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.statusBar().showMessage('Processing Image')
            self.dsGen.StoreImage(frame, name)
            self._image_counter += 1
            self.usernameLabel.setText(self.userName + " " + str(self._image_counter))
            self.statusBar().showMessage('Ready')
    
    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        try:
            if len(img.shape)==3 :
                if img.shape[2]==4:
                    qformat = QtGui.QImage.Format_RGBA8888
                else:
                    qformat = QtGui.QImage.Format_RGB888
            outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
            outImage = outImage.rgbSwapped()
            if window:
                self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))
        except:
            print("Camera Closed")
        
    def ReturnClicked(self):
        self._image_counter = 0
        self.destroy_webcam()
        self.clicked.emit()
        
        
        
        
        
        