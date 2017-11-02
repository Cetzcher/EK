from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTextEdit, QGroupBox, QLineEdit, QPushButton, QFormLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class UserListView(QWidget):

    def __init__(self, parent, users):
        QWidget.__init__(self, parent)
        layout = QFormLayout()


        for u in users:
            group = QGroupBox()
            g_layout = QHBoxLayout()
            group.setLayout(g_layout)
            g_layout.addWidget(QPushButton("Add to chat"))
            g_layout.addWidget(QPushButton("Start new chat"))

            layout.addRow(QLabel(str(u)), group)

        refresh = QPushButton("Refresh")
        #refresh.clicked.connect(self.parent())
        layout.addRow(refresh)
        self.setLayout(layout)
