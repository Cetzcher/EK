from PyQt5.QtWidgets import QWidget, QLabel, QFormLayout, \
    QLineEdit, QPushButton, QGroupBox, \
    QHBoxLayout, QGridLayout, QVBoxLayout, \
    QTableWidget, QTableWidgetItem, QTextEdit, QScrollArea

from PyQt5.QtCore import Qt

from client.app.views.chatListView import ChatListView
from client.app.views.currentChatView import CurrentChatView
from client.app.views.userListView import UserListView


class ChatView(QWidget):

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

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(pal)
        print("shwoing chat")

        layout = QGridLayout()
        self.setLayout(layout)

        self.__widgets = []
        self.__chat_list = None
        self.__chat_current = None
        self.__user_list = None

        self.update_all(["None"], [], [])

    def update_all(self, chats, users, cur_chat):
        layout = self.layout()
        for widget in self.__widgets:
            layout.removeWidget(widget)
            widget.setParent(None)


        self.__chat_list = ChatListView (self, chats)
        self.__chat_current = CurrentChatView(self, cur_chat)
        self.__user_list = UserListView(self, users)

        lp = QScrollArea()
        lp.setWidget( self.__chat_list)
        layout.addWidget(lp, 0, 0)
        lp.setMinimumWidth(350)

        layout.addWidget(self.__chat_current, 0, 1)

        ul = QScrollArea()
        ul.setWidget(self.__user_list)
        ul.setMinimumWidth(390)
        layout.addWidget(ul, 0, 2)

        self.__widgets = [self.__chat_list,  self.__user_list,  self.__chat_current]

    def on_send_msg(self, msg):
        self.__controller.send(msg)

    def update_text(self, msg):
        self.__chat_current.chatbox.setText(self.__chat_current.chatbox.toPlainText() + "\n" + msg)

