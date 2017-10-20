from PyQt5.QtWidgets import QWidget, QLabel, QFormLayout, QLineEdit, QPushButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RegisterView(QWidget):

    def __init__(self, controller):
        super().__init__()
        self.init_ui()
        self.show()
        self.__controller = controller

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

        loginHeader = QLabel("REGISTER")
        loginHeader.setFont(font)
        loginHeader.setAlignment(Qt.AlignCenter)

        layout.addWidget(loginHeader)
        # create form group
        layout.addWidget(self.create_group())
        to_login = QPushButton("already have an account? > login")
        to_login.clicked.connect(lambda: self.__controller.to_login())
        layout.addWidget(to_login)

    def create_group(self):
        group = QGroupBox()
        group_layout = QFormLayout()
        group.setLayout(group_layout)

        uinput = QLineEdit()
        pwinput = QLineEdit()
        pw_repeat = QLineEdit()
        email = QLineEdit()

        group_layout.setVerticalSpacing(30)
        group_layout.setHorizontalSpacing(120)

        group_layout.addRow( QLabel("USERNAME"), uinput)
        group_layout.addRow(QLabel("EMAIL"), email)
        group_layout.addRow(QLabel("PASSWORD"), pwinput)
        group_layout.addRow(QLabel("REPEAT PW"), pw_repeat)

        sub = QPushButton("submit")
        sub.clicked.connect(lambda: self.__controller.on_submit(uinput.text(),
                                                                pwinput.text(),
                                                                pw_repeat.text(),
                                                                email.text()))
        group_layout.addRow(sub)

        return group