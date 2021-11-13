# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrainModelWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrainModelWindow(object):
    def setupUi(self, TrainModelWindow):
        TrainModelWindow.setObjectName("TrainModelWindow")
        TrainModelWindow.resize(477, 380)
        self.verticalLayoutWidget = QtWidgets.QWidget(TrainModelWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 421, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowTitlelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.windowTitlelabel.setFont(font)
        self.windowTitlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.windowTitlelabel.setWordWrap(True)
        self.windowTitlelabel.setObjectName("windowTitlelabel")
        self.verticalLayout.addWidget(self.windowTitlelabel)
        self.instructionLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.instructionLabel.setFont(font)
        self.instructionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionLabel.setWordWrap(True)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout.addWidget(self.instructionLabel)
        self.startPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startPushButton.sizePolicy().hasHeightForWidth())
        self.startPushButton.setSizePolicy(sizePolicy)
        self.startPushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.startPushButton.setObjectName("startPushButton")
        self.verticalLayout.addWidget(self.startPushButton)
        self.backPushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backPushButton.sizePolicy().hasHeightForWidth())
        self.backPushButton.setSizePolicy(sizePolicy)
        self.backPushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.backPushButton.setObjectName("backPushButton")
        self.verticalLayout.addWidget(self.backPushButton)
        self.shellOutputTextEdit = QtWidgets.QTextEdit(TrainModelWindow)
        self.shellOutputTextEdit.setGeometry(QtCore.QRect(30, 200, 421, 161))
        self.shellOutputTextEdit.setReadOnly(True)
        self.shellOutputTextEdit.setObjectName("shellOutputTextEdit")
        self.outputLabel = QtWidgets.QLabel(TrainModelWindow)
        self.outputLabel.setGeometry(QtCore.QRect(30, 180, 81, 16))
        self.outputLabel.setObjectName("outputLabel")

        self.retranslateUi(TrainModelWindow)
        QtCore.QMetaObject.connectSlotsByName(TrainModelWindow)

    def retranslateUi(self, TrainModelWindow):
        _translate = QtCore.QCoreApplication.translate
        TrainModelWindow.setWindowTitle(_translate("TrainModelWindow", "Model Training Window"))
        self.windowTitlelabel.setText(_translate("TrainModelWindow", "Method description Label"))
        self.instructionLabel.setText(_translate("TrainModelWindow", "Please click start button to start training the model"))
        self.startPushButton.setText(_translate("TrainModelWindow", "Start"))
        self.backPushButton.setText(_translate("TrainModelWindow", "Back"))
        self.outputLabel.setText(_translate("TrainModelWindow", "Shell Output:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrainModelWindow = QtWidgets.QDialog()
    ui = Ui_TrainModelWindow()
    ui.setupUi(TrainModelWindow)
    TrainModelWindow.show()
    sys.exit(app.exec_())

