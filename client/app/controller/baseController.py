
class BaseController:

    def __init__(self, model, parent):
        self._model = model
        self._parent = parent

    def set_view(self, view):
        self._view = view

    def handle(self, json):
        raise NotImplemented

    def request(self, func):
        if callable(func):
            return self._parent.make_request(func)
        raise Exception()
