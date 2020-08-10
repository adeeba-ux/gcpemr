import PySide2.QtWidgets as qtW
import sys

import ProntoPlus.Views as Views
import ProntoPlus.ViewHandlers as vHandler


class MainVHandler(Views.main.Ui_MainWindow, qtW.QMainWindow):

    def __init__(self, config, session):
        super().__init__()
        self.setupUi(self)
        self.setup_buttons()
        self.main_widget.parent().layout()
        self._current_widget = self.main_widget
        self.cfg = config
        self.session = session
        self.open_patients_page()

    def setup_buttons(self):
        self.exit_btn.clicked.connect(sys.exit)
        # self.patients_btn.clicked.connect(self.open_patients_page)
        # self.options_btn.clicked.connect(self.open_options_page)

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

    @staticmethod
    def load_error_msg(error_title, msg, error):
        error_titles = {
            'Validation': 'Erro de Validação',
            'Save': 'Erro ao salvar.'
        }

        msgbox = qtW.QMessageBox()
        msgbox.setIcon(qtW.QMessageBox.Warning)
        msgbox.setText(error_titles.get(error_title))
        msgbox.setInformativeText(msg)
        msgbox.setDetailedText(str(error))
        msgbox.button(qtW.QMessageBox.Ok)
        msgbox.adjustSize()
        msgbox.exec_()
