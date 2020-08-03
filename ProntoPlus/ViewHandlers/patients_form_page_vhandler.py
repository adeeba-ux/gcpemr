import PySide2.QtWidgets as qtW

import ProntoPlus.Views as views
import ProntoPlus.ViewHandlers as vhandler


class PatientFormPageVHandler(views.patients_form_page.Ui_patients_form_page, qtW.QWidget):
    def __init__(self, parent: qtW.QMainWindow = None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setup_buttons()

    def setup_buttons(self):
        self.save_btn.clicked.connect(self._save)
        self.cancel_btn.clicked.connect(self._cancel)

    def _save(self):
        pass

    def _cancel(self):
        pass
