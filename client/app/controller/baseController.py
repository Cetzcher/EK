

class BaseController:
    """
    Base class for the controller.
    """

    def __init__(self, model, parent):
        """
        :param model: an instance of the model
        :param parent: the parent controller see controller/controller.py
        """
        self._model = model
        self._parent = parent

    def set_view(self, view):
        """
        Sets the view, called by parent controller
        :param view: an instance of some QWidget.
        :return: None
        """
        self._view = view

    def handle(self, args):
        """
        Handles a request made by 'request()'
        :param args:
        :return:
        """
        # args0 is the json result, args1 is the attached data if any
        raise NotImplementedError()

    def request(self, func):
        if callable(func):
            return self._parent.make_request(func)
        raise Exception()
