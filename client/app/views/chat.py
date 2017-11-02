from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton

from client.app.views.currentChatView import CurrentChatView


class ChatView(QWidget):

    def __init__(self, controller):
        super().__init__()

        self.__chat_current = None
        self.init_ui()
        self.show()
        self.__controller = controller


    def init_ui(self):

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(pal)
        print("shwoing chat")

        layout = QGridLayout()
        self.setLayout(layout)
        self.__chat_current = CurrentChatView(self, "")
        layout.addWidget(self.__chat_current, 0, 0)
        logout = QPushButton("logout")
        logout.clicked.connect(lambda : self.__controller.logout())
        layout.addWidget(logout)


    def on_send_msg(self, msg):
        self.__controller.send(msg)

    def update_text(self, msg):
        self.__chat_current.chatbox.setText(self.__chat_current.chatbox.toPlainText() + "\n" + msg)
