from client.app.controller.login import LoginController
from client.app.controller.register import RegisterController
from client.app.requestMaker import RequestMaker
from client.app.views.login import LoginView
from client.app.views.register import RegisterView


class Controller:

    def __init__(self, main_window, model):
        self.__mw = main_window
        # start at the login view so create one.
        self.__cur_view = None
        self.__cur_controller = None
        self.__model = model
        self.__request_thread = RequestMaker()
        self.__request_thread.callback.connect(self.__on_request_fin)
        self.__request_thread.start()

        self.show_register()

    def __on_request_fin(self, req):
        try:
            self.__cur_controller.handle(req)  # let the current controller handle the request.
        except Exception as e:
            print(e)

    def make_request(self, req):
        self.__request_thread.make_request(req)

    def show_login(self):
        controller = LoginController(self.__model, self)
        self.__cur_view = LoginView(controller)
        controller.set_view(self.__cur_view)
        self.__cur_controller = controller
        self.__mw.switch_to(self.__cur_view)

    def show_register(self):
        controller = RegisterController(self.__model, self)
        self.__cur_view = RegisterView(controller)
        controller.set_view(self.__cur_view)
        self.__cur_controller = controller
        self.__mw.switch_to(self.__cur_view)

    def show_chats(self):
        pass

    def show_single_chat(self):
        pass

    def show_user_list(self):
        pass