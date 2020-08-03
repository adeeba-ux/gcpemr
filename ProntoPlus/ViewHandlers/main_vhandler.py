import PySide2.QtWidgets as qtW
import sys

import ProntoPlus.Views as Views
import ProntoPlus.ViewHandlers as vHandler


class MainVHandler(Views.main.Ui_MainWindow, qtW.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_buttons()
        self.main_widget.parent().layout()
        self._current_widget = self.main_widget

    def setup_buttons(self):
        self.exit_btn.clicked.connect(sys.exit)
        self.patients_btn.clicked.connect(self.open_patients_page)
        self.options_btn.clicked.connect(self.open_options_page)

    def load_page(self, page):
        self.mainArea.removeWidget(self._current_widget)
        self._current_widget.close()
        self.mainArea.addWidget(page)
        self.mainArea.update()
        self._current_widget = page

    def open_patients_page(self):
        page = vHandler.patients_page_vhandler.PatientsPageVHandler(self)
        self.load_page(page)

    def open_options_page(self):
        pass
