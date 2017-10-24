from PyQt5 import QtCore
import queue
import websocket

class WebsocketHandler(QtCore.QThread):

    msg_recv_callback = QtCore.pyqtSignal(object)
    err_callback = QtCore.pyqtSignal(object)

    def __init__(self, url):
        QtCore.QThread.__init__(self)
        self.__send_q = queue.Queue()
        self.__ws = None
        self.__url = url

    class sender(QtCore.QThread):

        def __init__(self, q):
            QtCore.QThread.__init__(self)
            self.__q = q
            self.__ws = None

        def start_with_args(self, ws):
            self.__ws = ws
            self.start()

        def run(self):
            while True:
                item = self.__q.get()
                self.__ws.send(item)

    def queue_message(self, msg):
        self.__send_q.put(msg)

    def __msg_recv(self, _, msg):
        #print("recv:", msg)
        self.msg_recv_callback.emit(msg)

    def __msg_err(self, _, err):
        print("error: ", err)
        self.err_callback.emit(err)

    def __close(self, ws):
        pass

    def run(self):
            while True:
                #websocket.enableTrace(True)
                ws = websocket.WebSocketApp(self.__url,
                                            on_message=self.__msg_recv,
                                            on_error=self.__msg_err,
                                            on_close=self.__close)

                sender = WebsocketHandler.sender(self.__send_q)
                ws.on_open = sender.start_with_args
                print("running webserver")
                ws.run_forever()

    def quit(self):
        QtCore.QThread.quit(self)
        self.__ws.close()








