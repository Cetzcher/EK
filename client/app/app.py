import sys
from PyQt5.QtWidgets import QApplication, QWidget

from client.app.controller.controller import Controller
from client.app.views.mainWindow import MainWindow
from client.app.models.model import Model
import os

from client.app.websocketHandler import WebsocketHandler


def main():
    app = QApplication(sys.argv)
    # setup MVC
    mw = MainWindow()
    Controller(mw, Model())
    mw.show()
    sys.exit(app.exec_())