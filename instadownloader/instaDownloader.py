# -*- coding: utf-8 -*-

# Import necessary modules from PyQt5 library for GUI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Import other required modules
import pytube
from pytube.cli import on_progress
import tkinter as tk
import requests
import threading
import re
import instaloader
import os

# PyQt5 UI code generated from 'instaDownloader.ui' using pyuic5
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        # ... (all the UI setup code here)
        # ...
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 551, 281))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #304352, stop:1 #d7d2cc);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 89, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_url = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_url.setGeometry(QtCore.QRect(63, 91, 311, 31))
        self.lineEdit_url.setStyleSheet("background-color:#d7d2cc;\n"
"border-radius : 10px;")
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(132, 30, 181, 31))
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
        self.pushButton_start = QtWidgets.QPushButton(self.frame)
        self.pushButton_start.setGeometry(QtCore.QRect(210, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color: #bdc3c7;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #948E99, stop:1 #2E1437);\n"
"}")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_min = QtWidgets.QPushButton(self.frame)
        self.pushButton_min.setGeometry(QtCore.QRect(455, 10, 18, 18))
        self.pushButton_min.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_min.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_min.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(509, 10, 18, 18))
        self.pushButton_close.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_close.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_close.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(255, 8, 8);\n"
"")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_max = QtWidgets.QPushButton(self.frame)
        self.pushButton_max.setGeometry(QtCore.QRect(482, 10, 18, 18))
        self.pushButton_max.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_max.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_max.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.pushButton_max.setText("")
        self.pushButton_max.setObjectName("pushButton_max")
        self.pushButton_paste = QtWidgets.QPushButton(self.frame)
        self.pushButton_paste.setGeometry(QtCore.QRect(410, 89, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_paste.setFont(font)
        self.pushButton_paste.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color: #bdc3c7;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #948E99, stop:1 #2E1437);\n"
"}")
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.pushButton_open = QtWidgets.QPushButton(self.frame)
        self.pushButton_open.setGeometry(QtCore.QRect(410, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color: #bdc3c7;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #948E99, stop:1 #2E1437);\n"
"}")
        self.pushButton_open.setObjectName("pushButton_open")
        self.label_sizeOfVideo = QtWidgets.QLabel(self.frame)
        self.label_sizeOfVideo.setGeometry(QtCore.QRect(549, 201, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_sizeOfVideo.setFont(font)
        self.label_sizeOfVideo.setStyleSheet("background-color: none;\n"
"")
        self.label_sizeOfVideo.setText("")
        self.label_sizeOfVideo.setObjectName("label_sizeOfVideo")
        self.lineEdit_parh = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_parh.setGeometry(QtCore.QRect(130, 150, 251, 31))
        self.lineEdit_parh.setStyleSheet("background-color:#d7d2cc;\n"
"border-radius : 10px;")
        self.lineEdit_parh.setObjectName("lineEdit_parh")
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
        # ... (translation setup code here)
        # ...
       
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "url :"))
        self.label_2.setText(_translate("MainWindow", "save to :"))
        self.label_3.setText(_translate("MainWindow", "instagram downloader"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_min.setToolTip(_translate("MainWindow", "<html><head/><body ><p>Minimize</p></body></html>"))
        self.pushButton_close.setToolTip(_translate("MainWindow", "Close"))
        self.pushButton_max.setToolTip(_translate("MainWindow", "Normal size"))
        self.pushButton_paste.setText(_translate("MainWindow", "Paste"))
        self.pushButton_open.setText(_translate("MainWindow", "Open"))


        global dir_path
        dir_path = "E:\\"
        self.lineEdit_parh.setText(dir_path)
        self.pushButton_paste.clicked.connect(self.paste_text)
        self.pushButton_open.clicked.connect(self.file_save)
        self.pushButton_start.clicked.connect(self.download_file)
        
    # Helper method to paste URL from clipboard into the URL input field
    def paste_text(self):
        root = tk.Tk()
        spam = root.clipboard_get()
        self.lineEdit_url.setText(spam)
        global url 
        url = self.lineEdit_url.text()
        
        
    # Helper method to select the directory for saving the downloaded files
    def file_save(self):
        global dir_path
        dir_path=QFileDialog.getExistingDirectory(self,"Choose Directory",dir_path)
        print(dir_path)
        self.lineEdit_parh.setText(dir_path)
    
    # Main method to download the file
    def download_file(self):
        print(url)
        print(dir_path)
        def download():
            # Change the working directory to the selected directory
            os.chdir(dir_path)

            # Create an instance of Instaloader to download Instagram content
            load = instaloader.Instaloader()
            load.login("___just_say___", "Wp123456789%")

            # Extract the post shortcode from the URL
            shortcode = re.findall(r'https:\/\/www\.instagram\.com\/\w+\/(\w+)' , url)

            # Download the post using the Instaloader library
            post = instaloader.Post.from_shortcode(load.context , shortcode[0])
            load.download_post(post , target=shortcode)
            print("done...!")
            
        # Start the download in a separate thread to avoid blocking the UI
        threading.Thread(target=download).start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
