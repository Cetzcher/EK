from PyQt5.QtWidgets import QWidget, QVBoxLayout


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.__active = None
        layout = QVBoxLayout()
        self.setLayout(layout)


    def switch_to(self, widget):
        """
        Switches out the current toplevel widget
        :param widget: an instance of QWidget
        :return: None
        """
        try:
            self.layout().removeWidget(self.__active)
            self.__active.setParent(None)
            print("removing:", self.__active)
        except Exception as e:
            pass
        self.__active = widget
        self.layout().addWidget(widget)