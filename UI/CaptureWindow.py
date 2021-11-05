# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptureWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaptureWindow(object):
    def setupUi(self, CaptureWindow):
        CaptureWindow.setObjectName("CaptureWindow")
        CaptureWindow.resize(381, 304)
        self.centralwidget = QtWidgets.QWidget(CaptureWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout.addWidget(self.imageLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.usernameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout.addWidget(self.usernameLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.capturePushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.capturePushButton.setObjectName("capturePushButton")
        self.horizontalLayout.addWidget(self.capturePushButton)
        self.returnPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.returnPushButton.setObjectName("returnPushButton")
        self.horizontalLayout.addWidget(self.returnPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        CaptureWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaptureWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        CaptureWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaptureWindow)
        self.statusbar.setObjectName("statusbar")
        CaptureWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CaptureWindow)
        QtCore.QMetaObject.connectSlotsByName(CaptureWindow)

    def retranslateUi(self, CaptureWindow):
        _translate = QtCore.QCoreApplication.translate
        CaptureWindow.setWindowTitle(_translate("CaptureWindow", "Capture"))
        self.imageLabel.setText(_translate("CaptureWindow", "Image"))
        self.usernameLabel.setText(_translate("CaptureWindow", "Username Label"))
        self.capturePushButton.setText(_translate("CaptureWindow", "Capture"))
        self.returnPushButton.setText(_translate("CaptureWindow", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaptureWindow = QtWidgets.QMainWindow()
    ui = Ui_CaptureWindow()
    ui.setupUi(CaptureWindow)
    CaptureWindow.show()
    sys.exit(app.exec_())

