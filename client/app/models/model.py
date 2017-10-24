from client.app.requestFactory import RequestFactory
from PyQt5 import QtCore

class Model:


    def __init__(self):
        self.__request_factory = RequestFactory()
        self.__tok = None
        self.__chats = []
        self.__chat_msgs = {}  # mapping of ID to content
        self.__users = []

    def get_request_factory(self):
        # returns the request factory
        return self.__request_factory

    def set_token(self, token):
        # sets the current token
        self.__tok = token

    def get_token(self):
        # gets the current token
        return self.__tok

    def get_chats(self):
        # gets a list of all chat ids
        return self.__chats

    def set_chats(self, chats):
        self.__chats = chats

    def get_users(self):
        return self.__users

    def set_users(self, users):
        self.__users = users

    def get_current_chat(self):
        return self.__chat_msgs

    def set_current_chat(self, msgs):
        self.__chat_msgs = msgs
