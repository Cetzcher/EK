from client.app.controller.baseController import BaseController


class RegisterController(BaseController):

    def __init__(self, model, view, parent_controller):
        BaseController.__init__(self, model, view, parent_controller)

    def request_register(self, user, pw, pw_again, email):
        if(pw != pw_again):
            return

        factory = self._model.get_request_factory()
        req = factory.register_request()



    def handle(self, json):
        # handle the json request upon login
        pass