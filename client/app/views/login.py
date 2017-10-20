from PyQt5.QtWidgets import QWidget, QLabel, QFormLayout, QLineEdit, QPushButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class LoginView(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(pal)

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont()
        font.setWeight(500)
        font.setPointSize(22)

        loginHeader = QLabel("LOGIN")
        loginHeader.setFont(font)
        loginHeader.setAlignment(Qt.AlignCenter)

        layout.addWidget(loginHeader)
        # create form group
        layout.addWidget(self.create_group())
        layout.addWidget(QPushButton("register"))

    def create_group(self):
        group = QGroupBox()
        group_layout = QFormLayout()
        group.setLayout(group_layout)

        ulabel = QLabel("USERNAME")
        uinput = QLineEdit()
        pwlable = QLabel("PASSWORD")
        pwinput = QLineEdit()

        group_layout.setVerticalSpacing(30)
        group_layout.setHorizontalSpacing(120)

        group_layout.addRow(ulabel, uinput)
        group_layout.addRow(pwlable, pwinput)
        group_layout.addRow(QPushButton("submit"))

        return group