from client.app.requestFactory import RequestFactory
from PyQt5 import QtCore

class Model:


    def __init__(self):
        self.__request_factory = RequestFactory()
        self.__tok = None
        self.__chat_ids = []
        self.__chat_msgs = {}  # mapping of ID to content
        self.__users = []

    def get_request_factory(self):
        # returns the request factory
        return self.__request_factory

    def set_token(self, token):
        # sets the current token
        self.__tok = token

    def get_chats(self):
        # gets a list of all chat ids
        return self.__chat_ids

    def get_users(self):
        return self.__users

    def get_token(self):
        # gets the current token
        return self.__tok

    def set_chats(self, chats):
        pass

    def set_users(self, users):
        self.__users = users

    def set_current_chat(self):
        pass
