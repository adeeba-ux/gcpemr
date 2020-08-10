import ProntoPlus.Views as Views
import ProntoPlus.Controllers as Ctrls

import PySide2.QtWidgets as qtW
import PySide2.QtCore as qCore
import PySide2.QtGui as qtGui
import typing as t
import datetime as dt
import uuid
import os
import configparser
import sqlalchemy.orm as orm

cfg = configparser.ConfigParser()
cfg.read('config.ini')


class RecordWriterVHandler(Views.record_writer_page.MainWindow, qtW.QMainWindow):

    def __init__(self, session: orm.Session, patient_data: t.Dict = None):
        super().__init__()
        self._session = session
        self.patient_ctrl = Ctrls.PatientCtrl(self._session)
        self.record_ctrl = Ctrls.RecordCtrl(self._session)

        if patient_data is not None:
            self.patient_data = patient_data
        else:
            self.patient_data = {}

    def setup_patient_data(self):
        data = self.patient_data.get('patient')
        record = self.patient_data.get('record')

        date = dt.datetime.now().strftime('%d-%m-%Y')
        patient_name = data.get('name')

        if data.get('birth_date') is not None:
            _birth = dt.date(*[int(v) for v in data.get('birth_date').split('-')])
            _today = dt.date.today()
            age = str(_today.year - _birth.year - ((_today.month, _today.day) < (_birth.month, _birth.day)))
        else:
            age = ''

        if age:
            if int(age) > 1:
                age = ' '.join([age, 'anos'])
            else:
                age = ' '.join([age, 'ano'])

        patient_gender = self.patient_ctrl.gender_to_string(data.get('gender'))

        self.patient_data_widget.date_output.setText(date)
        self.patient_data_widget.patient_name_output.setText(patient_name)
        self.patient_data_widget.age_output.setText(age)
        self.patient_data_widget.gender_output.setText(patient_gender)

        self.editor.setText(record.text)
        self._just_loaded = True
        self.saved = True

    def save_record(self):
        record_text = self.editor.toHtml()
        record = self.patient_data.get('record')
        record.text = record_text
        record.last_modified_date = dt.datetime.now()

        updated = self.record_ctrl.add(record)
        if updated:
            self.saved = True
        else:
            self.dialog_critical(updated[1])

    def closeEvent(self, event):
        check_saved_msg = "O pronturário foi modificado desde a última vez que foi salvo."
        question = "Deseja salva-lo antes de fechar?"

        msg_box = qtW.QMessageBox()
        msg_box.setText(check_saved_msg)
        msg_box.setInformativeText(question)
        msg_box.setStandardButtons(qtW.QMessageBox.Yes | qtW.QMessageBox.No | qtW.QMessageBox.Abort)

        sim_btn = msg_box.button(qtW.QMessageBox.Yes)
        sim_btn.setText('Sim')
        nao_btn = msg_box.button(qtW.QMessageBox.No)
        nao_btn.setText('Não')

        cancel_btn = msg_box.button(qtW.QMessageBox.Abort)
        cancel_btn.setText('Cancelar')

        if not self.saved:
            msg_box.exec_()

            if msg_box.clickedButton() == sim_btn:
                self.save_record()
                event.accept()
            elif msg_box.clickedButton() == cancel_btn:
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()
