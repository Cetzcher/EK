from PyQt5 import QtCore

import queue
import json

class RequestMaker(QtCore.QThread):
    """
    Runs request functions and executes a callback with the results
    """

    callback = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.__q = queue.Queue()

    def make_request(self, req_function, **kwargs):
        """
        puts the request into the request Q
        :param req_function: a callable object with a single retunr value
              that can be interpreted using json.loads(return_value)
        :param kwargs: any amount of key value pairs; ATM they will be passed through
                in case the caller wants the callback to get any further information
        :return: None
        """
        # request should be functions from the requestFactory
        print("putting item")
        item = req_function, kwargs
        self.__q.put(item)

    def run(self):
        while True:
            item = self.__q.get()
            func, data = item
            try:
                result = func()  # run the query
                dic = json.loads(result.text, result.status_code)
                self.callback.emit((dic, data))
            except Exception as e:
                print("ERROR IN RQ MAKER" + str(e))
                print(e.__traceback__)
                self.callback.emit((None, {}))

