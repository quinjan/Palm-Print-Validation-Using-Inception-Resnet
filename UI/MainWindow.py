# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 192)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 421, 171))
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
        self.generateDatasetPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateDatasetPushButton.sizePolicy().hasHeightForWidth())
        self.generateDatasetPushButton.setSizePolicy(sizePolicy)
        self.generateDatasetPushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.generateDatasetPushButton.setObjectName("generateDatasetPushButton")
        self.verticalLayout.addWidget(self.generateDatasetPushButton)
        self.trainModelPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainModelPushButton.sizePolicy().hasHeightForWidth())
        self.trainModelPushButton.setSizePolicy(sizePolicy)
        self.trainModelPushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.trainModelPushButton.setObjectName("trainModelPushButton")
        self.verticalLayout.addWidget(self.trainModelPushButton)
        self.validateUserPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateUserPushButton.sizePolicy().hasHeightForWidth())
        self.validateUserPushButton.setSizePolicy(sizePolicy)
        self.validateUserPushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.validateUserPushButton.setObjectName("validateUserPushButton")
        self.verticalLayout.addWidget(self.validateUserPushButton)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.windowTitlelabel.setText(_translate("MainWindow", "Palm Print Verification"))
        self.headerLabel.setText(_translate("MainWindow", "Project By: Quinjan Robert R. Ocampo & Darien  Rhyce B. Soria"))
        self.generateDatasetPushButton.setText(_translate("MainWindow", "Generate Dataset"))
        self.trainModelPushButton.setText(_translate("MainWindow", "Train Model"))
        self.validateUserPushButton.setText(_translate("MainWindow", "Validate User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

