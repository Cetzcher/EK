from PyQt5 import QtCore
import time

LIST_USERS = "LIST_USERS"
LIST_CHATS = "LIST_CHATS"
CUR_CHAT = "CUR_CHAT"

class UpdateWorker(QtCore.QThread):


    def __init__(self, updateable, request_maker, interval=1000):
        """

        Updates any updateable object that is: the updateable must provide the
        following methods:
            update_available_chats
            update_users
            update_chat_contents
        as well as:
            get_request_factory

        :param updateable:
        :param request_maker:
        :param interval:
        """
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
            self.__updateable.update_available_chats(json)  # parse data here ?
        elif res_type == LIST_USERS:
            self.__updateable.update_users(json)
        elif res_type == CUR_CHAT:
            self.__updateable.update_chat_contents(1, 2)
        else:
            return

    def run(self):


        while True:
            time.sleep(self.__sleep_time)
            # create the requests
            tok = self.__updateable.get_token()
            ids = self.__updateable.get_chats()

            users_req = self.__req_factory.list_user_request()
            chats_req = self.__req_factory.list_chats_request(tok)
            chats = [(self.__req_factory.read_chat_request(tok, i), i) for i in range(ids)]  # get all chats.


            # sent request to the request maker

            self.__req_maker.make_request(users_req, req_name=LIST_USERS)
            self.__req_maker.make_request(chats_req, req_name=LIST_CHATS)
            # send all chat requests and order them
            order = 0
            for item in chats:
                req, chat_id = item  # get request function and id.
                self.__req_maker.make_request(req, req_name=CUR_CHAT, order=order, chat_id=chat_id)
                order += 1
