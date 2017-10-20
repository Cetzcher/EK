import requests


class RequestFactory:
    """
    Create request functions that can be carried out at some later point
    each function returns a lambda expression, when called they will make a blocking request
    to the REST api, they should not be directly from the GUI thread, but instead be handed
    over to the RequestMaker
    """

    def __init__(self, base_url="http://localhost:3030/api"):
        self.__url = base_url

    def login_request(self, user, passw):
        return lambda: requests.post(self.__url + "/authenticate",
                                     {"name": user,
                                      "password": passw})

    def register_request(self, user, passw, email):
        return lambda: requests.post(self.__url + "/register",
                                     {"name": user,
                                      "password": passw,
                                      "email": email})

    def list_user_request(self):
        return lambda: requests.get(self.__url + "/users")

    def list_chats_request(self, token):
        return lambda: requests.post(self.__url + "/auth/list_chats",
                                     { "token": token })

    def start_chat_request(self, token, other_user):
        return lambda: requests.post(self.__url + "/auth/start_chat/" + str(other_user),
                                     { "token": token })

    def read_chat_request(self, token, chat_id):
        return lambda: requests.post(self.__url + "/auth/read/" + str(chat_id),
                                     { "token": token })

    def read_all_chat_request(self, token, chat_id):
        return lambda: requests.post(self.__url + "/auth/read_all/" + str(chat_id),
                                     { "token": token })

    def send_chat_request(self, token, chat_id, text):
        return lambda: requests.post(self.__url + "/auth/send/" + str(chat_id),
                                     { "token": token, "msg": text })


