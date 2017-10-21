from PyQt5.QtWidgets import QWidget, QLabel, QFormLayout, QLineEdit, QPushButton, QGroupBox, QHBoxLayout

class ChatView(QWidget):

    def __init__(self, controller):
        super().__init__()
        self.init_ui()
        self.show()
        self.__controller = controller

    def create_chat_list_view(self):
        group = QGroupBox()
        layout = QFormLayout()
        group.setLayout(layout)

        layout.addRow(QLabel("CHAT1"))
        layout.addRow(QLabel("CHAT2"))
        layout.addRow(QLabel("CHAT3"))
        layout.addRow(QLabel("CHAT4"))
        layout.addRow(QLabel("CHAT5"))

        return group

    def create_user_list_view(self):
        group = QGroupBox()
        layout = QFormLayout()
        group.setLayout(layout)

        layout.addRow(QLabel("user1"), QPushButton("add to chats"))
        layout.addRow(QLabel("user2"), QPushButton("add to chats"))
        layout.addRow(QLabel("user3"), QPushButton("add to chats"))
        layout.addRow(QLabel("user4"), QPushButton("add to chats"))
        layout.addRow(QLabel("user5"), QPushButton("add to chats"))

        return group

    def create_chat_view(self):
        group = QGroupBox()
        layout = QFormLayout()
        group.setLayout(layout)

        layout.addRow(QLabel("TEXT"), QPushButton("RESP"))
        layout.addRow(QLabel("TEXT"), QPushButton("REsp"))
        layout.addRow(QLabel("TEXT"), QPushButton("RESP"))

        return group


    def init_ui(self):
        print("shwoing chat")

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.create_chat_list_view())
        layout.addWidget(self.create_chat_view())
        layout.addWidget(self.create_user_list_view())