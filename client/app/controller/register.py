from client.app.controller.baseController import BaseController
from PyQt5.QtWidgets import QMessageBox
import re

class RegisterController(BaseController):

    # STACK OVERFLOW: https://stackoverflow.com/questions/8022530/python-check-for-valid-email-address
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self, model, parent_controller):
        BaseController.__init__(self, model, parent_controller)

    def on_submit(self, user, pw, pw_again, email, url):
        # called when the form is submitted
        print("submitting")
        err = ""
        if pw != pw_again:
            err += "passwords do not match"
        if not RegisterController.check_email(email):
            err += "\nemail is not valid"

        if err:
            QMessageBox.about(self._view, "error", err)


        print("creating request")
        factory = self._model.get_request_factory()
        factory.set_url(url)
        req = factory.register_request(user, pw, email)
        print("requesting: " + str(req))
        self.request(req)  # send request, wait on callback in handle.


    def to_login(self):
        # switches view to login
        self._parent.show_login()

    @staticmethod
    def check_email(mail):
        return RegisterController.EMAIL_REGEX.match(mail)

    def handle(self, *args):
        # handle the json request upon login
        json = args[0]
        print("== RESULT ==")
        print("args:")
        print(args)
        print(json)
        if(bool(json["success"])):
            self._parent.show_login()
        else:
            err = json["error"]
            QMessageBox.about(self._view, "error", err)