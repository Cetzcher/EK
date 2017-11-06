# test the app using regression tests, login and register are already done in postman.
# so the only relevant part is the websocket connection, this involves connecting, sending, and receiving
# messages.
import client.app.requestFactory as req_fac
import client.app.requestMaker as req_maker
import client.app.websocketHandler as websocketHandler
import sys
from PyQt5.QtWidgets import QApplication, QWidget
import queue


# setup a dummy QT app since threading wont work otherwise.
app = QApplication(sys.argv)

factory = req_fac.RequestFactory()
factory.set_url("http://localhost:9001/api")
create_user = factory.register_request("regression_user", "regression_pw", "reggresion.m@email.com")
login_user = factory.login_request("regression_user", "regression_pw")
request_maker = req_maker.RequestMaker()

# test the login
def test_req_maker(args):
    json, keywords = args
    print(json, keywords)
    if keywords["test"] == "LOGIN":
        print("testing login")
        assert json["success"] == True
        print("success")

# test the websocket
def test_websocket(args):
    print("testing webscoket send/recv")
    assert args == "You are now connected to the chat!"
    print("successful")


request_maker.callback.connect(lambda x: test_req_maker(x))
request_maker.start()
request_maker.make_request(create_user, test="REGISTER")
request_maker.make_request(login_user, test="LOGIN")

ws = websocketHandler.WebsocketHandler("ws://localhost:9001/api/echo", {"token":"$2a$04$VReK9zJ49EEuHrjEZPb.TEST_USER.fg4ErqOguOuTa2Zs669t1e"})
ws.msg_recv_callback.connect(lambda x: test_websocket(x))
ws.start()


sys.exit(app.exec_())

