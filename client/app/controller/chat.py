from PyQt5.QtCore import QTimer, Qt

from client.app.controller.baseController import BaseController
from client.app.websocketHandler import WebsocketHandler

LIST_USERS = "LIST_USERS"
LIST_CHATS = "LIST_CHATS"
CUR_CHAT = "CUR_CHAT"

class ChatController(BaseController):

    def __init__(self, model, parent_controller):
        BaseController.__init__(self, model, parent_controller)
        # start a timer to periodically update the GUI
        self.__factory = self._model.get_request_factory()
        self.__ws_handler = WebsocketHandler("ws://localhost:3030/api/echo")
        self.__ws_handler.msg_recv_callback.connect(self.msg_recv)
        self.__ws_handler.start()

    def send(self, msg):
        self.__ws_handler.queue_message(msg)

    def msg_recv(self, msg):
        # get text from chat box.
        # append msg to it
        self._view.update_text(msg)