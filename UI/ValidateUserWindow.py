# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ValidateUserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ValidateUserWindow(object):
    def setupUi(self, ValidateUserWindow):
        ValidateUserWindow.setObjectName("ValidateUserWindow")
        ValidateUserWindow.resize(381, 339)
        self.centralwidget = QtWidgets.QWidget(ValidateUserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.methodDescriptionLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methodDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.methodDescriptionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.methodDescriptionLabel.setFont(font)
        self.methodDescriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.methodDescriptionLabel.setObjectName("methodDescriptionLabel")
        self.verticalLayout.addWidget(self.methodDescriptionLabel)
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
        ValidateUserWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ValidateUserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        ValidateUserWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ValidateUserWindow)
        self.statusbar.setObjectName("statusbar")
        ValidateUserWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ValidateUserWindow)
        QtCore.QMetaObject.connectSlotsByName(ValidateUserWindow)

    def retranslateUi(self, ValidateUserWindow):
        _translate = QtCore.QCoreApplication.translate
        ValidateUserWindow.setWindowTitle(_translate("ValidateUserWindow", "Validate User"))
        self.methodDescriptionLabel.setText(_translate("ValidateUserWindow", "Method Description"))
        self.imageLabel.setText(_translate("ValidateUserWindow", "Image"))
        self.usernameLabel.setText(_translate("ValidateUserWindow", "Username Label"))
        self.capturePushButton.setText(_translate("ValidateUserWindow", "Capture"))
        self.returnPushButton.setText(_translate("ValidateUserWindow", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ValidateUserWindow = QtWidgets.QMainWindow()
    ui = Ui_ValidateUserWindow()
    ui.setupUi(ValidateUserWindow)
    ValidateUserWindow.show()
    sys.exit(app.exec_())

