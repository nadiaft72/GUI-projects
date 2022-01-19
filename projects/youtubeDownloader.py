# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtubeDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pytube
from pytube.cli import on_progress
import tkinter as tk
import requests

class Ui_youtubeDownloaderWindow(QWidget):
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 761, 421))
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
        self.label_2.setGeometry(QtCore.QRect(7, 273, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit_parh = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_parh.setGeometry(QtCore.QRect(69, 273, 301, 31))
        self.lineEdit_parh.setStyleSheet("background-color:#d7d2cc;\n"
"border-radius : 10px;")
        self.lineEdit_parh.setObjectName("lineEdit_parh")
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
        self.pushButton_start.setGeometry(QtCore.QRect(320, 354, 101, 31))
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
        self.pushButton_min.setGeometry(QtCore.QRect(670, 10, 18, 18))
        self.pushButton_min.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_min.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_min.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(724, 10, 18, 18))
        self.pushButton_close.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_close.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_close.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(255, 8, 8);\n"
"")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_max = QtWidgets.QPushButton(self.frame)
        self.pushButton_max.setGeometry(QtCore.QRect(697, 10, 18, 18))
        self.pushButton_max.setMinimumSize(QtCore.QSize(18, 18))
        self.pushButton_max.setMaximumSize(QtCore.QSize(18, 18))
        self.pushButton_max.setStyleSheet("border-radius:8px;\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.pushButton_max.setText("")
        self.pushButton_max.setObjectName("pushButton_max")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(8, 202, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none;\n"
"")
        self.label_4.setObjectName("label_4")
        self.comboBox_quality = QtWidgets.QComboBox(self.frame)
        self.comboBox_quality.setGeometry(QtCore.QRect(66, 202, 401, 27))
        self.comboBox_quality.setStyleSheet("background-color:none\n"
"")
        self.comboBox_quality.setObjectName("comboBox_quality")
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
        self.pushButton_open.setGeometry(QtCore.QRect(410, 273, 101, 31))
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
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(490, 201, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: none;\n"
"")
        self.label_5.setObjectName("label_5")
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
        self.label_videoTitle = QtWidgets.QLabel(self.frame)
        self.label_videoTitle.setGeometry(QtCore.QRect(100, 150, 571, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_videoTitle.setFont(font)
        self.label_videoTitle.setStyleSheet("background-color: none;\n"
"text-align: center;\n"
"")
        self.label_videoTitle.setText("")
        self.label_videoTitle.setObjectName("label_videoTitle")
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
        self.label.setText(_translate("MainWindow", "url :"))
        self.label_2.setText(_translate("MainWindow", "save to :"))
        self.label_3.setText(_translate("MainWindow", "Youtube downloader"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_min.setToolTip(_translate("MainWindow", "<html><head/><body ><p>Minimize</p></body></html>"))
        self.pushButton_close.setToolTip(_translate("MainWindow", "Close"))
        self.pushButton_max.setToolTip(_translate("MainWindow", "Normal size"))
        self.label_4.setText(_translate("MainWindow", "quality :"))
        self.pushButton_paste.setText(_translate("MainWindow", "Paste"))
        self.pushButton_open.setText(_translate("MainWindow", "Open"))
        self.label_5.setText(_translate("MainWindow", "size :"))





        global dir_path
        dir_path = "I:\\"
        self.lineEdit_parh.setText(dir_path)
        self.pushButton_paste.clicked.connect(self.paste_text)
        self.comboBox_quality.activated[str].connect(self.onActivated)                  # +++
        self.pushButton_open.clicked.connect(self.file_save)
        self.pushButton_start.clicked.connect(self.download_file)

    def paste_text(self):
        root = tk.Tk()
        spam = root.clipboard_get()
        self.lineEdit_url.setText(spam)
        global url 
        url = self.lineEdit_url.text()
        self.internet_on()

    def internet_on(self):
        url = "http://www.google.com"
        timeout = 5.
        try:
            request = requests. get(url, timeout=timeout)
            self.show_streams()

        except (requests. ConnectionError, requests. Timeout) as exception:
            self.label_videoTitle.setText("please check your connection...!")

    def show_streams(self):

        global yt ,listOfStreams
        yt = pytube.YouTube(url,on_progress_callback=on_progress)
        title = yt.streams.get_highest_resolution().title
        self.label_videoTitle.setText(title)
        listOfStreams = list()
        
        for stream in yt.streams:
            print(stream)
            itag =  stream.itag 
            mime_type = stream.mime_type
            abr_audio = stream.abr
            type = stream.type
            if type == "video" :
                quality = resolution_video = stream.resolution
                fps = stream.fps
                string = title + " , "+ mime_type + " , "+ str(quality) +" , " + str(fps) +"fps" 

            else :
                quality = abr_audio
                string = title + " , "+ mime_type + " , "+ str(quality)

            listOfStreams.append(string)
        self.comboBox_quality.addItems(listOfStreams)

    def onActivated(self , text):
        global itag , video
        print("the text is  :  "+text)
        if text in listOfStreams:
                itag = listOfStreams.index(text)
        itag = yt.streams[itag].itag
        video = yt.streams.get_by_itag(itag)
        sizeOfVideo = video.filesize/1024/1024

        self.label_sizeOfVideo.setText("{:.2f}".format(sizeOfVideo)+"mb")


              
    def file_save(self):
        global dir_path
        dir_path=QFileDialog.getExistingDirectory(self,"Choose Directory",dir_path)
        print(dir_path)
        self.lineEdit_parh.setText(dir_path)


    def download_file(self):
        print("itag : "+ str(itag))
        print(type(itag))
        print(url)
        print(dir_path)
        print(dir_path)
        video.download(dir_path) 
        print("done...!")


