
class BaseController:

    def __init__(self, view, model, parent):
        self._view = view
        self._model = model
        self._parent = parent

    def handle(self, json):
        raise NotImplemented

    def request(self, func):
        if callable(func):
            return self._parent.make_request(func)
        raise Exception()
