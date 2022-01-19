
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainMenu import Ui_MainMenu
from passwordGenerator import Ui_PasswordGenerator
from youtubeDownloader import Ui_youtubeDownloaderWindow


class YoutubeDownloader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_youtubeDownloaderWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.setupUi(self)

    def mousePressEvent(self, evt):
        """Select the toolbar."""
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()


class PasswordGenerator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_PasswordGenerator()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.setupUi(self)

    def mousePressEvent(self, evt):
        """Select the toolbar."""
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.pushButton_passwordGenerator.clicked.connect(self.passwordGenerator)
        self.ui.pushButton_youtubeDownloader.clicked.connect(self.youtubeDownloader)

        self.show()

    def mousePressEvent(self, evt):
        """Select the toolbar."""
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def passwordGenerator(self):
        self.passwordGenerator = PasswordGenerator()
        self.passwordGenerator.show()
        self.close() 
    def youtubeDownloader(self):
        self.youtubeDownloader = YoutubeDownloader()
        self.youtubeDownloader.show()
        self.close()



if __name__== "__main__":
    import sys 
    app = QApplication(sys.argv)
    root = RootMain()
    root.show()
    sys.exit(app.exec_())