from client.app.requestFactory import RequestFactory
from PyQt5 import QtCore

class Model:

    on_update = QtCore.pyqtSignal()

    def __init__(self):
        self.__request_factory = RequestFactory()
        self.__tok = None
        self.__chat_ids = []
        self.__chat_msgs = {}  # mapping of ID to content

    def get_request_factory(self):
        # returns the request factory
        return self.__request_factory

    def set_token(self, token):
        # sets the current token
        self.__tok = token

    def get_chats(self):
        # gets a list of all chat ids
        return self.__chat_ids

    def get_token(self):
        # gets the current token
        return self.__tok

    def update_chat_contents(self, chat_id, content):
        # updates the contents of a chat
        pass

    def update_users(self, userlist):
        # updates the list of existing users
        pass

    def update_available_chats(self, chatlist):
        # updates the list of chats that are availible to the user
        pass