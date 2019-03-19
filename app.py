import Hamming
from mainwindow import Ui_Hamming
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from window import MyWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = MyWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.onLoad()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

main()

