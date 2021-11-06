# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:37:33 2021

@author: quinj
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.TrainModelWindow import Ui_TrainModelWindow
from Common.MachineLearningModel import MachineLearningModel
import sys

class TrainerWorker(QtCore.QThread):
    def __init__(self, selectedMethod, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.selectedMethod = selectedMethod
    
    def run(self):
        self.machineLearning = MachineLearningModel(self.selectedMethod)
        self.machineLearning.Train()
    
    def stop(self):
        self.terminate()


class TrainModelWindow(QtWidgets.QDialog, Ui_TrainModelWindow):
    
    clicked = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(TrainModelWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.trainerWorker = QtCore.QThread()
        
        self.trainerWorker.finished.connect(self.ShowTrainingFinishedDialog)
        self.backPushButton.clicked.connect(self.BackButtonClicked)
        self.startPushButton.clicked.connect(self.StartStopButtonClicked)     
    
    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.shellOutputTextEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.shellOutputTextEdit.setTextCursor(cursor)
        self.shellOutputTextEdit.ensureCursorVisible()
    
    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
    
    def StartStopButtonClicked(self):
        if(self.startPushButton.text() == "Start"):
            self.StartTraining()
        else:
            self.StopTraining()

    def StartTraining(self):
        self.shellOutputTextEdit.clear()
        self.startPushButton.setText("Stop")
        self.trainerWorker = TrainerWorker(self.selectedMethod)
        self.backPushButton.setEnabled(False)
        self.trainerWorker.start()
    
    def StopTraining(self):
        self.trainerWorker.stop()
        self.startPushButton.setText("Start")
        self.backPushButton.setEnabled(True)
        self.normalOutputWritten("Training Stopped!")
        
    def BackButtonClicked(self):
        self.clicked.emit()
        
    def ShowTrainingFinishedDialog(self):
        self.backPushButton.setEnabled(True)
        self.startPushButton.setText("Start")
        QtWidgets.QMessageBox.information(self, "Done!", "Training Done")
        
        