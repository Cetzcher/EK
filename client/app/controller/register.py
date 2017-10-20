from client.app.controller.baseController import BaseController


class RegisterController(BaseController):

    def __init__(self, model, parent_controller):
        BaseController.__init__(self, model, parent_controller)

    def on_submit(self, user, pw, pw_again, email):
        print("submitting")
        if(pw != pw_again):
            return

        print("creating request")
        factory = self._model.get_request_factory()
        req = factory.register_request(user, pw, email)
        print("requesting: " + str(req))
        self.request(req)  # send request, wait on callback in handle.


    def to_login(self):
        self._parent.show_login()

    def handle(self, args):
        # handle the json request upon login
        json = args[0]
        print("== RESULT ==")
        print("args:")
        print(args)
        print(json)