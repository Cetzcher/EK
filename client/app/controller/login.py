from client.app.controller.baseController import BaseController


class LoginController(BaseController):

    def __init__(self, model, parent_controller):
        BaseController.__init__(self, model, parent_controller)

    def login(self, user, pw):
        factory = self._model.get_request_factory()
        req = factory.login_request(user, pw)
        self.request(req)

    def handle(self, *args):
        # handle the json request upon login
        json = args[0]
        print("== RESULT ==")
        print(json)

    def to_register(self):
        self._parent.show_register()