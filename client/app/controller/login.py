from client.app.controller.baseController import BaseController


class LoginController(BaseController):

    def __init__(self, model, parent_controller):
        BaseController.__init__(self, model, parent_controller)

    def login(self, user, pw):
        # handle press of submit button on login form
        factory = self._model.get_request_factory()
        req = factory.login_request(user, pw)
        self.request(req)
        print("LOGGING IN")

    def handle(self, *args):
        # handle request reult.
        # handle the json request upon login
        json = args[0]
        print("== RESULT ==")
        print(json)
        success = json["success"]
        if(bool(success)):
            tok = json["token"]
            self._model.set_token(tok)
            self._parent.show_chat()
        else:
            err = json["error"]
            print(err)



    def to_register(self):
        # called upon clicking the 'to register' button. Switches to the register view
        self._parent.show_register()