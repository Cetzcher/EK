from PyQt5 import QtCore

import queue
import json

class RequestMaker(QtCore.QThread):

    callback = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.__q = queue.Queue()

    def make_request(self, req_function):
        # request should be functions from the requestFactory
        self.__q.put(req_function)

    def run(self):
        while True:
            item = self.__q.get()
            try:
                result = item()  # run the query
            except Exception as e:
                result = "{error:" + str(e) + "}"
            dic = json.loads(result)
            self.callback.emit(dic)
