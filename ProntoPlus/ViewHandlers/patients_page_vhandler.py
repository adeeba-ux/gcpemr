import PySide2.QtWidgets as qtW
import PySide2.QtCore as qCore
import PySide2.QtGui as qGui
import typing as t
import sqlalchemy as sa

import ProntoPlus.Views as Views
import ProntoPlus.ViewHandlers as vHandler
import ProntoPlus.Controllers as Ctrls


class PatientsPageVHandler(Views.patients_page.Ui_patients_page, qtW.QWidget):
    def __init__(self, parent: vHandler.MainVHandler = None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.patient_ctrl = Ctrls.init_patient_ctrl()
        self.record_ctrl = Ctrls.init_record_ctrl()
        self.presentation_fields = self.patient_ctrl.presentation()
        self.cls = self.patient_ctrl.CTRLCLASS
        self._current_patients_cache = []

        self.show_table()
        self.setup_buttons_and_menu()
        self.writer = vHandler.RecordWriterVHandler()

    def setup_buttons_and_menu(self):
        self.patient_search_btn.clicked.connect(self._search)
        self.patient_add_btn.clicked.connect(self._add_patient)
        self.patient_edit_btn.clicked.connect(self._add_patient_with_payload)
        self.patient_record_add_btn.clicked.connect(self._open_record)

        self.patient_table.doubleClicked.connect(self._open_record)
        self.patient_table.customContextMenuRequested.connect(self.setup_table_context_menu)
        self.patient_table.itemSelectionChanged.connect(self.toggle_menu_buttons)
        # self.patient_table.isItemSelected.connect(self.toggle_menu_buttons)

    def toggle_menu_buttons(self):
        self.patient_record_add_btn.setEnabled(True)
        self.patient_edit_btn.setEnabled(True)

    def setup_table_context_menu(self, position):
        menu = qtW.QMenu()
        edit_action = menu.addAction("Editar")
        delete_action = menu.addAction("Apagar paciente")
        record_action = menu.addAction("Abrir Prontuário")

        action = menu.exec_(self.patient_table.mapToGlobal(position))
        if action == edit_action:
            self._add_patient_with_payload()
        elif action == record_action:
            self._open_record()
        elif action == delete_action:
            self._delete_patient()

    def show_table(self, rows: t.Dict = []):
        if not rows:
            rows = self._search_patients()

        self.patient_table.setRowCount(0)
        self.patient_table.setColumnCount(len(self.presentation_fields))

        columns = []
        for column_name in self.presentation_fields.values():
            column = qtW.QTableWidgetItem()
            column.setText(column_name)
            columns.append(column)

        for col_nbr, col_item in enumerate(columns):
            self.patient_table.setHorizontalHeaderItem(col_nbr, col_item)

        if rows:
            self.patient_table.setRowCount(len(rows))
            row_nbr = 0
            for row in rows:
                for column_nbr, column_name in enumerate(self.presentation_fields.keys()):
                    self.patient_table.setItem(row_nbr, column_nbr, qtW.QTableWidgetItem(row.get(column_name)))
                row_nbr += 1

        self.patient_table.resizeColumnsToContents()

    def _get_current_patient(self):
        return self._current_patients_cache[self.patient_table.currentRow()]

    def _search_patients(self, query_filter: str = ''):
        if not query_filter:
            patients_to_dump = self.patient_ctrl.get_all().all()
        else:
            patients_to_dump = self.patient_ctrl.get_all().filter(sa.or_(
                self.cls.name.like('%' + str(query_filter) + '%'),
                self.cls.cpf.like('%' + str(query_filter) + '%')
            )).all()
        rows = self.patient_ctrl.dump(patients_to_dump, many=True)

        self._current_patients_cache = rows
        return rows

    def _add_patient(self):
        page = vHandler.patients_form_page_vhandler.PatientFormPageVHandler(self.parent)
        self.parent.load_page(page)

    def _add_patient_with_payload(self):
        data = self.patient_ctrl.load(self._get_current_patient())
        page = vHandler.patients_form_page_vhandler.PatientFormPageVHandler(self.parent, data)
        page.setup_patient_data()
        self.parent.load_page(page)

    def _delete_patient(self):
        data = self.patient_ctrl.load(self._get_current_patient())

        confirmation = qtW.QMessageBox()
        confirmation.setText(f'Tem certeza de que deseja deletar {data.name}?')
        confirmation.setStandardButtons(qtW.QMessageBox.Yes | qtW.QMessageBox.No)

        sim_btn = confirmation.button(qtW.QMessageBox.Yes)
        sim_btn.setText('Sim')
        nao_btn = confirmation.button(qtW.QMessageBox.No)
        nao_btn.setText('Não')

        confirmation.exec_()

        if confirmation.clickedButton() == sim_btn:
            deletion = self.patient_ctrl.delete(data)
            if not isinstance(deletion, list):
                self.show_table()
            else:
                self.parent.load_error_msg('Delete', '', deletion[1])

    def _search(self):
        filter_txt = self.patient_search_input.text()
        data = self._search_patients(filter_txt)
        self.show_table(data)

    def _open_record(self):
        data = {
            'patient': self._get_current_patient()
        }
        data['record'] = self.record_ctrl.get_from_patient(data['patient']['id'], data['patient']['tenant'])

        self.writer.patient_data = data
        self.writer.setup_patient_data()
        self.writer.show()

