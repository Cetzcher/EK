from client.app.requestFactory import RequestFactory


class Model:

    def __init__(self):
        self.__request_factory = RequestFactory()

    def get_request_factory(self):
        return self.__request_factory