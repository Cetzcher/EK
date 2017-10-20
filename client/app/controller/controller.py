from client.app.controller.login import LoginController
from client.app.controller.register import RegisterController
from client.app.requestMaker import RequestMaker
from client.app.views.login import LoginView
from client.app.views.register import RegisterView

class Controller:
    """
    Parent controller of the UI, handles changes of the view and
    dispatches results from the request thread to the sub controller
    """

    def __init__(self, main_window, model):
        """
        Initializes the controller and packs the window
        :param main_window: an instance of the first widget created since this automatically
               packs as the main window.
        :param model: the model
        """
        self.__mw = main_window
        # start at the login view so create one.
        self.__cur_view = None
        self.__cur_controller = None
        self.__model = model
        self.__request_thread = RequestMaker()
        self.__request_thread.callback.connect(self.__on_request_fin)
        self.__request_thread.start()

        self.show_register()

    def __on_request_fin(self, req):
        """
        Called whenever a request finishes, dispatches to the current controller
        :param req: the request result, a tuple of (JSON, DATA) whereas DATA is
               a associative array of key value pairs.
        :return: None
        """
        try:
            self.__cur_controller.handle(req)  # let the current controller handle the request.
        except Exception as e:
            print(e)

    def make_request(self, req):
        """
        Helper for making requests to the request worker thread
        :param req: the request to be executed by the thread
        :return: None
        """
        self.__request_thread.make_request(req)

    def __show(self, controllerT, viewT):
        """
        Helper for switching views, dynamically creates view and controller object
        :param controllerT: A type which __init__  method satisfies the following signature
                (model, parentController);
        :param viewT: A type which is a subclass of QWidget and satisfies the __init__ method
                of (view)
        :return: None
        """
        controller = controllerT(self.__model, self)
        self.__cur_view = viewT(controller)
        controller.set_view(self.__cur_view)
        self.__cur_controller = controller
        self.__mw.switch_to(self.__cur_view)

    def show_login(self):
        # shows the login view
        self.__show(LoginController, LoginView)

    def show_register(self):
        # shows the register view
        self.__show(RegisterController, RegisterView)

    def show_chats(self):
        pass

    def show_single_chat(self):
        pass

    def show_user_list(self):
        pass