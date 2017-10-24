from PyQt5.QtCore import QTimer, Qt

from client.app.controller.baseController import BaseController


LIST_USERS = "LIST_USERS"
LIST_CHATS = "LIST_CHATS"
CUR_CHAT = "CUR_CHAT"

class ChatController(BaseController):

    def __init__(self, model, parent_controller):
        BaseController.__init__(self, model, parent_controller)
        # start a timer to periodically update the GUI
        timer = QTimer()
        timer.setInterval(300)
        timer.setTimerType(Qt.CoarseTimer)
        timer.timeout.connect(self.__on_tick)
        self.__timer = timer
        self.__factory = self._model.get_request_factory()

        timer.start()


    def __on_tick(self):
        # set the requests
        tok = self._model.get_token()
        ids = self._model.get_chats()

        users_req = self.__factory.list_user_request()
        chats_req = self.__factory.list_chats_request(tok)
        chats = [(self.__factory.read_chat_request(tok, i), i) for i in ids]  # get all chats.


        # sent request to the request maker
        self.request(users_req, req_type=LIST_USERS)
        self.request(chats_req, req_type=LIST_CHATS)
        # send all chat requests and order them
        order = 0
        for item in chats:
            req, chat_id = item  # get request function and id.
            self.request(req, req_type=CUR_CHAT, order=order, chat_id=chat_id)
            order += 1

    def handle(self, *args):
        json = args[0]
        dat = args[1]
        print("got data: ", json, "data", dat)
        req_type = dat["req_type"]
        print("REQUEST DATA:", req_type)
        if req_type == LIST_CHATS:
            chats = json["chats"]
            self._model.set_chats(chats)
        elif req_type == LIST_USERS:
            users = json["user_names"]
            self._model.set_users(users)
        elif req_type == CUR_CHAT:
            pass

        # TODO impl self._view.update_all(self._model.get_chats() , self._model.get_users(), ["a", "b", "c", "d"])

