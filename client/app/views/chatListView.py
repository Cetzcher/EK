from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit, QGroupBox, QLineEdit, QPushButton, QFormLayout
from PyQt5.QtCore import Qt


class ChatListView(QWidget):
    def __init__(self, parent, chats):
        QWidget.__init__(self, parent)
        layout = QFormLayout()

        for c in chats:
            layout.addRow(QLabel(str(c)), QPushButton("Show"))

        self.setLayout(layout)
