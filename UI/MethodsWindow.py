# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MethodsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MethodsWindow(object):
    def setupUi(self, MethodsWindow):
        MethodsWindow.setObjectName("MethodsWindow")
        MethodsWindow.resize(439, 192)
        self.verticalLayoutWidget = QtWidgets.QWidget(MethodsWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowTitlelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.windowTitlelabel.setFont(font)
        self.windowTitlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.windowTitlelabel.setWordWrap(True)
        self.windowTitlelabel.setObjectName("windowTitlelabel")
        self.verticalLayout.addWidget(self.windowTitlelabel)
        self.headerLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setWordWrap(True)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.method1PushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method1PushButton.sizePolicy().hasHeightForWidth())
        self.method1PushButton.setSizePolicy(sizePolicy)
        self.method1PushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.method1PushButton.setObjectName("method1PushButton")
        self.verticalLayout.addWidget(self.method1PushButton)
        self.method2PushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method2PushButton.sizePolicy().hasHeightForWidth())
        self.method2PushButton.setSizePolicy(sizePolicy)
        self.method2PushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.method2PushButton.setObjectName("method2PushButton")
        self.verticalLayout.addWidget(self.method2PushButton)
        self.method3PushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method3PushButton.sizePolicy().hasHeightForWidth())
        self.method3PushButton.setSizePolicy(sizePolicy)
        self.method3PushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.method3PushButton.setObjectName("method3PushButton")
        self.verticalLayout.addWidget(self.method3PushButton)
        self.backPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backPushButton.setObjectName("backPushButton")
        self.verticalLayout.addWidget(self.backPushButton)

        self.retranslateUi(MethodsWindow)
        QtCore.QMetaObject.connectSlotsByName(MethodsWindow)

    def retranslateUi(self, MethodsWindow):
        _translate = QtCore.QCoreApplication.translate
        MethodsWindow.setWindowTitle(_translate("MethodsWindow", "Dialog"))
        self.windowTitlelabel.setText(_translate("MethodsWindow", "Palm Print Verification"))
        self.headerLabel.setText(_translate("MethodsWindow", "Project By: Quinjan Robert R. Ocampo & Darien  Rhyce B. Soria"))
        self.method1PushButton.setText(_translate("MethodsWindow", "CLAHE and Guassian Smoothing"))
        self.method2PushButton.setText(_translate("MethodsWindow", "2D Histogram EQ and Morphological Closing"))
        self.method3PushButton.setText(_translate("MethodsWindow", "Sobel Edge Detection"))
        self.backPushButton.setText(_translate("MethodsWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MethodsWindow = QtWidgets.QDialog()
    ui = Ui_MethodsWindow()
    ui.setupUi(MethodsWindow)
    MethodsWindow.show()
    sys.exit(app.exec_())

