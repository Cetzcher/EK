from client.app.controller.baseController import BaseController

class ChatController(BaseController):

    def __init__(self, model, parent_controller):
        BaseController.__init__(self, model, parent_controller)
