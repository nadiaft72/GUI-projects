# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainWindow):
        # Set up the main window with the specified size
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        # Set up the style sheet for the frame (background color)
        self.frame.setGeometry(QtCore.QRect(9, 9, 391, 421))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #304352, stop:1 #d7d2cc);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 181, 31))
        # Set up the font and style for the label
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: none;")
        self.label_3.setObjectName("label_3")
        self.pushButton_passwordGenerator = QtWidgets.QPushButton(self.frame)
        self.pushButton_passwordGenerator.setGeometry(QtCore.QRect(40, 110, 161, 31))
        # Set up the font and style for the "passwordGenerator" button
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_passwordGenerator.setFont(font)
        self.pushButton_passwordGenerator.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color: #bdc3c7;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #948E99, stop:1 #2E1437);\n"
"}")
        self.pushButton_passwordGenerator.setObjectName("pushButton_passwordGenerator")
        # ... (additional code for the rest of the UI elements)
        # ...
        self.pushButton_min = QtWidgets.QPushButton(self.frame)
        self.pushButton_min.setGeometry(QtCore.QRect(306, 10, 18, 18))
        self.pushButton_min.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_min.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_min.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(360, 10, 18, 18))
        self.pushButton_close.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_close.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_close.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(255, 8, 8);\n"
"")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_max = QtWidgets.QPushButton(self.frame)
        self.pushButton_max.setGeometry(QtCore.QRect(333, 10, 18, 18))
        self.pushButton_max.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_max.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_max.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.pushButton_max.setText("")
        self.pushButton_max.setObjectName("pushButton_max")
        self.pushButton_youtubeDownloader = QtWidgets.QPushButton(self.frame)
        self.pushButton_youtubeDownloader.setGeometry(QtCore.QRect(40, 160, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_youtubeDownloader.setFont(font)
        self.pushButton_youtubeDownloader.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color: #bdc3c7;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #948E99, stop:1 #2E1437);\n"
"}")
        self.pushButton_youtubeDownloader.setObjectName("pushButton_youtubeDownloader")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close)
        self.pushButton_max.clicked.connect(MainWindow.showNormal)
        self.pushButton_min.clicked.connect(self.pushButton_min.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "projects :"))
        self.pushButton_passwordGenerator.setText(_translate("MainWindow", "passwordGenerator"))
        self.pushButton_min.setToolTip(_translate("MainWindow", "<html><head/><body ><p>Minimize</p></body></html>"))
        self.pushButton_close.setToolTip(_translate("MainWindow", "Close"))
        self.pushButton_max.setToolTip(_translate("MainWindow", "Normal size"))
        self.pushButton_youtubeDownloader.setText(_translate("MainWindow", "youtubeDownloader"))


