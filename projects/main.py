
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainMenu import Ui_MainMenu
from passwordGenerator import Ui_PasswordGenerator
from youtubeDownloader import Ui_youtubeDownloaderWindow

# Define the YoutubeDownloader class, which is a QMainWindow.
class YoutubeDownloader(QMainWindow):
    def __init__(self):
        # Initialize the QMainWindow and set up the UI from the youtubeDownloader module.
        QMainWindow.__init__(self)
        self.ui = Ui_youtubeDownloaderWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)# Remove the window frame (title bar).
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make the window background translucent.

        # Connect the buttons from the main menu to their respective functions.
        self.ui.setupUi(self)

    def mousePressEvent(self, evt):
        """Select the toolbar."""
        # This event is triggered when the mouse button is pressed.
        # It is used to select the toolbar to enable dragging the window.
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""
        # This event is triggered when the mouse is moved.
        # It is used to move the window with the mouse iteration.
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

# Define the PasswordGenerator class, which is a QMainWindow.
class PasswordGenerator(QMainWindow):
    def __init__(self):
        # Initialize the QMainWindow and set up the UI from the passwordGenerator module.
        QMainWindow.__init__(self)
        self.ui = Ui_PasswordGenerator()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.setupUi(self)

    def mousePressEvent(self, evt):
        """Select the toolbar."""
        # This event is triggered when the mouse button is pressed.
        # It is used to select the toolbar to enable dragging the window.
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""
        # This event is triggered when the mouse is moved.
        # It is used to move the window with the mouse iteration.
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

# Define the RootMain class, which is the main QMainWindow for the application.
class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Connect the buttons from the main menu to their respective functions.
        self.ui.pushButton_passwordGenerator.clicked.connect(self.passwordGenerator)
        self.ui.pushButton_youtubeDownloader.clicked.connect(self.youtubeDownloader)

        self.show()

    def mousePressEvent(self, evt):
        """Select the toolbar."""
        # This event is triggered when the mouse button is pressed.
        # It is used to select the toolbar to enable dragging the window.
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""
        # This event is triggered when the mouse is moved.
        # It is used to move the window with the mouse iteration.
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def passwordGenerator(self):
        # This function is called when the "Password Generator" button is clicked.
        # It creates a new PasswordGenerator window and closes the main menu.
        self.passwordGenerator = PasswordGenerator()
        self.passwordGenerator.show()
        self.close() 
        
    def youtubeDownloader(self):
        # This function is called when the "Youtube Downloader" button is clicked.
        # It creates a new YoutubeDownloader window and closes the main menu.
        self.youtubeDownloader = YoutubeDownloader()
        self.youtubeDownloader.show()
        self.close()


# The application starts here.
if __name__== "__main__":
    import sys 
    app = QApplication(sys.argv)
    root = RootMain()
    root.show()
    sys.exit(app.exec_())
