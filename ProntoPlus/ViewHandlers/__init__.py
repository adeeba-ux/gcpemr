from .main_vhandler import MainVHandler
from .patients_page_vhandler import PatientsPageVHandler
from .patients_form_page_vhandler import PatientFormPageVHandler
from .record_writer_vhandler import RecordWriterVHandler

import PySide2.QtWidgets as qtW
import sys
import uuid


def start(cfg):
    app = qtW.QApplication(sys.argv)
    app.setStyle('Breeze')
    window = main_vhandler.MainVHandler(cfg)
    window.TENANT = uuid.UUID(cfg['CLIENT']['tenant'])
    window.show()
    sys.exit(app.exec_())


