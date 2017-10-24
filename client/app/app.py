import sys
from PyQt5.QtWidgets import QApplication, QWidget

from client.app.controller.controller import Controller
from client.app.views.mainWindow import MainWindow
from client.app.models.model import Model
import os

from client.app.websocketHandler import WebsocketHandler


def main():
    # read style sheet
    s = ""
    """
    with open(os.path.dirname(__file__) + "/style.css") as file:
        for line in file.readlines():
            s += line + " "
    """

    app = QApplication(sys.argv)
    app.setStyleSheet(s)
    # setup MVC
    mw = MainWindow()
    Controller(mw, Model())
    mw.show()
    sys.exit(app.exec_())