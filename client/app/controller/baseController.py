
class BaseController:

    def __init__(self, model, parent):
        self._model = model
        self._parent = parent

    def set_view(self, view):
        self._view = view

    def handle(self, args):
        # args0 is the json result, args1 is the attached data if any
        raise NotImplemented

    def request(self, func):
        if callable(func):
            return self._parent.make_request(func)
        raise Exception()
