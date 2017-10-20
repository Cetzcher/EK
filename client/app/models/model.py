from client.app.requestFactory import RequestFactory


class Model:

    def __init__(self):
        self.__request_factory = RequestFactory()

    def get_request_factory(self):
        return self.__request_factory

    def get_token(self):
        pass

    def get_cur_chat(self):
        pass

    def update_chats(self, json):
        pass

    def update_users(self, json):
        pass

    def update_current_chat(self, json):
        pass