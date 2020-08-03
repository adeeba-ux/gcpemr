import ProntoPlus.ViewHandlers as vHandler
import ProntoPlus.Views as Views
import ProntoPlus.Controllers as Ctrls

import PySide2.QtWidgets as qtW


class RecordWriterVHandler(Views.record_writer_page.MainWindow, qtW.QMainWindow):

    def __init__(self, patient_data):
        super().__init__()
        self.patient_data = patient_data
