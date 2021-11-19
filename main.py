# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 18:35:27 2021

@author: quinj
"""
import PyQt5
from PyQt5 import QtWidgets
from UI.MainWindowMethods import MainWindow  
import cv2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    def destroyWindow():
        cv2.destroyAllWindows()
        app.exec_()
    sys.exit(destroyWindow())