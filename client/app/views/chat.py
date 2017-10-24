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

        #chatlist = ChatListView(self, ["chat1", "chat2", "chat3"])
        #userlist = UserListView(self, ["user1", "user2", "user3"])
        #curchat = CurrentChatView(self, ["msg1", "msg2"])

        #layout.addWidget(chatlist, 0, 0)
        #layout.addWidget(curchat, 0, 1)
        #layout.addWidget(userlist, 0, 2)

        #self.__widgets = [chatlist, userlist, curchat]
        self.__widgets = []
        self.update_all(["chat1", "chat2", "chat3"], ["user1", "user2", "user3"], [{"msg": "hello friend", "sent_by": "pierre"}])

    def update_all(self, chats, users, cur_chat):
        layout = self.layout()
        for widget in self.__widgets:
            layout.removeWidget(widget)
            widget.setParent(None)

        chatlist = ChatListView (self, chats)
        userlist = UserListView(self, users)
        curchat = CurrentChatView(self, cur_chat)

        lp = QScrollArea()
        lp.setWidget(chatlist)
        layout.addWidget(lp, 0, 0)

        layout.addWidget(curchat, 0, 1)

        ul = QScrollArea()
        ul.setWidget(userlist)
        layout.addWidget(ul, 0, 2)

        self.__widgets = [chatlist, userlist, curchat]

