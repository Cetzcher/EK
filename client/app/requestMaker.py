from PyQt5 import QtCore

import queue
import json

class RequestMaker(QtCore.QThread):

    callback = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.__q = queue.Queue()

    def make_request(self, req_function, **kwargs):
        # request should be functions from the requestFactory
        item = req_function, kwargs
        self.__q.put(item)

    def run(self):
        while True:
            item = self.__q.get()
            func, data = item
            try:
                result = func()  # run the query
            except Exception as e:
                print("ERROR IN RQ MAKER" + str(e))
                print(e.__traceback__)
                result = object() # workaround
                result.__dict__["text"] = "{'error':" + str(e) + "}"
                result.__dict__["status_code"] = 500
            print(result.text, result.status_code)
            dic = json.loads(result.text, result.status_code)
            self.callback.emit((dic, data))
