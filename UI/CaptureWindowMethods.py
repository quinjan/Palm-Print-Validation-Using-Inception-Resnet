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
import time

class FrameGrabber(QtCore.QThread):
    def __init__(self, parent=None):
        super(FrameGrabber, self).__init__(parent)

    signal = QtCore.pyqtSignal(np.ndarray)
    
    cameraLoaded = QtCore.pyqtSignal(bool)

    def run(self):
        #Uncomment for RPI
        #os.system('sudo modprobe bcm2835-v4l2')

        self.cap = cv2.VideoCapture("http://raspberrypi:5000/video_feed")
        time.sleep(5)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
        
        if(self.cap.isOpened()):
            self.ThreadActive = True
            self.cameraLoaded.emit(True)
        
        else:
            self.ThreadActive = False
        
        while self.ThreadActive:
            success, frame = self.cap.read()
            if success:
                self.signal.emit(frame)
        self.cap.release()
        self.quit()
    
    def stop(self):
        self.ThreadActive = False
                
class Processor(QtCore.QThread):
    def __init__(self, imageDictionary, selectedMethod, userName, parent=None):
        super(Processor, self).__init__(parent)
        self.imageDictionary = imageDictionary
        self.dsGen = DatasetGenerator(selectedMethod , userName)
        self.dsGen.InitializeDatasetFolder()
        self.dsGen.DeleteCurrentUserDataset()
    
    signal = QtCore.pyqtSignal()
    
    def run(self):
        for name, image in self.imageDictionary.items():
            print("Processing image: " + name)
            self.dsGen.StoreImage(image, name)
            print("Processing image: " + name + "Done.")
        self.signal.emit()
        
    def stop(self):
        self.terminate()
    
        
class CaptureWindow(QtWidgets.QMainWindow, Ui_CaptureWindow):
    
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CaptureWindow, self).__init__(parent)
        self.setupUi(self)

        self.grabber = QtCore.QThread()
        self.imageProcessor = QtCore.QThread()
        self.imageProcessor.finished.connect(self.ProcessFinished)
        
        self.statusBar().showMessage('Ready')
        self.returnPushButton.clicked.connect(self.ReturnClicked)
        self.capturePushButton.clicked.connect(self.capture_image)
        self.processPushButton.clicked.connect(self.ProcessImage)
        
        self.imageLabel.setScaledContents(True)
        self._image_counter = 0
        self.imageToProcess = {}
    
    def start_webcam(self):
        print("Starting Webcam")
        self.imageLabel.setText("Loading Camera......")
        self.capturePushButton.setEnabled(False)
        self.processPushButton.setEnabled(False)
        
        self.grabber = FrameGrabber()
        self.grabber.cameraLoaded.connect(self.CameraInitialized)
        self.grabber.signal.connect(self.update_frame)
        self.grabber.start()
        
        self.dsGen = DatasetGenerator(self.selectedMethod , self.userName)
        self.dsGen.InitializeDatasetFolder()
        self.usernameLabel.setText(self.userName + " " + str(self._image_counter))
    
    @QtCore.pyqtSlot(bool)
    def CameraInitialized(self, isCameraInitialized):
        if(isCameraInitialized):
            self.capturePushButton.setEnabled(True)
            self.processPushButton.setEnabled(True)

    def destroy_webcam(self):
        print("Destroying Camera")
        self.grabber.stop()

    @QtCore.pyqtSlot(np.ndarray)
    def update_frame(self, frame):
        self.frame = frame
        self.displayImage(self.frame)

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

    @QtCore.pyqtSlot()
    def capture_image(self):
        QtWidgets.QApplication.beep()
        
        name = "{}.png".format(self._image_counter)
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.imageToProcess[name] = self.frame
        print("Captured: " + self.userName + " " + str(self._image_counter))
        
        self._image_counter += 1
        self.usernameLabel.setText(self.userName + " " + str(self._image_counter))
        
    def ProcessImage(self):
        if(bool(self.imageToProcess)):
            self.imageProcessor = Processor(self.imageToProcess, self.selectedMethod, self.userName)
            self.imageProcessor.signal.connect(self.ProcessFinished)
            self.capturePushButton.setEnabled(False)
            self.processPushButton.setEnabled(False)
            self.statusBar().showMessage('Processing Image')
            self.imageProcessor.start()
        else:
            QtWidgets.QMessageBox.critical(self, "Error!", "No Image To Process.")

    @QtCore.pyqtSlot()
    def ProcessFinished(self):
        self.capturePushButton.setEnabled(True)
        self.processPushButton.setEnabled(True)
        self.statusBar().showMessage('Ready')
        QtWidgets.QMessageBox.information(self, "Done!", "Processing Done")
            
    def ReturnClicked(self):
        self.destroy_webcam()
        
        self._image_counter = 0
        self.imageToProcess = {}
        self.processTextEdit.clear()
        
        self.clicked.emit()
    
    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.processTextEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.processTextEdit.setTextCursor(cursor)
        self.processTextEdit.ensureCursorVisible()
        
        
        
        
        
        