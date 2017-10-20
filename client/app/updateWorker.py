from PyQt5 import QtCore
import time

LIST_USERS = "LIST_USERS"
LIST_CHATS = "LIST_CHATS"
CUR_CHAT = "CUR_CHAT"

class UpdateWorker(QtCore.QThread):

    def __init__(self, updateable, request_maker, interval=1000):
        QtCore.QThread.__init__(self)
        # updateable must provide a token
        # thread runs some requests every interval and updates them to the updateable object
        # interval in ms
        self.__updateable = updateable
        self.__req_factory = updateable.get_request_factory()
        self.__sleep_time = interval / 1000
        self.__req_maker = request_maker
        self.__req_maker.callback.connect(self.__handle)

    def __handle(self, args):
        # collect answers and update the updatable
        json, data = args
        res_type = data["req_name"] if "req_name" in data else None
        if not res_type:
            return
        elif res_type == LIST_CHATS:
            self.__updateable.update_chats(json)  # parse data here ?
        elif res_type == LIST_USERS:
            self.__updateable.update_users(json)
        elif res_type == CUR_CHAT:
            self.__updateable.update_current_chat()
        else:
            return

    def run(self):


        while True:
            time.sleep(self.__sleep_time)
            # create the requests
            tok = self.__updateable.get_token()
            cur_chat_id = self.__updateable.get_cur_chat()

            users_req = self.__req_factory.list_user_request()
            chats_req = self.__req_factory.list_chats_request(tok)
            cur_chat_req = self.__req_factory.read_chat_request(tok, cur_chat_id)
            # sent request to the request maker

            self.__req_maker.make_request(users_req, req_name=LIST_USERS)
            self.__req_maker.make_request(chats_req, req_name=LIST_CHATS)
            self.__req_maker.make_request(cur_chat_req, req_name=CUR_CHAT)
