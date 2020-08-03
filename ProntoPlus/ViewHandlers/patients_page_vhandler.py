import PySide2.QtWidgets as qtW
import PySide2.QtCore as qCore
import PySide2.QtGui as qGui
import typing as t
import sqlalchemy as sa

import ProntoPlus.Views as Views
import ProntoPlus.ViewHandlers as vHandler
import ProntoPlus.Controllers as Ctrls


class PatientsPageVHandler(Views.patients_page.Ui_patients_page, qtW.QWidget):
    def __init__(self, parent: qtW.QMainWindow = None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.controller = Ctrls.init_patient_ctrl()
        self.presentation_fields = self.controller.presentation()
        self.cls = self.controller.CTRLCLASS
        self._current_patients_cache = []

        self.show_table()
        self.setup_buttons_and_menu()

    def setup_buttons_and_menu(self):
        self.patient_search_btn.clicked.connect(self._search)
        self.patient_add_btn.clicked.connect(self._add_patient)
        self.patient_edit_btn.clicked.connect(self._add_patient_with_payload)
        self.patient_record_add_btn.clicked.connect(self._open_record)

        self.patient_table.doubleClicked.connect(self._add_patient_with_payload)
        self.patient_table.customContextMenuRequested.connect(self.setup_table_context_menu)
        self.patient_table.itemSelectionChanged.connect(self.toggle_menu_buttons)
        # self.patient_table.isItemSelected.connect(self.toggle_menu_buttons)

    def toggle_menu_buttons(self):
        self.patient_record_add_btn.setEnabled(True)
        self.patient_edit_btn.setEnabled(True)

    def setup_table_context_menu(self, position):
        menu = qtW.QMenu()
        edit_action = menu.addAction("Editar")
        record_action = menu.addAction("Abrir Prontuário")

        action = menu.exec_(self.patient_table.mapToGlobal(position))
        if action == edit_action:
            self._add_patient_with_payload()
        elif action == record_action:
            self._open_record()

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

    def _get_current_row_data(self):
        return self._current_patients_cache[self.patient_table.currentRow()]

    def _search_patients(self, query_filter: str = ''):
        if not query_filter:
            patients_to_dump = self.controller.get_all().all()
        else:
            patients_to_dump = self.controller.get_all().filter(sa.or_(
                self.cls.name.like('%' + str(query_filter) + '%'),
                self.cls.cpf.like('%' + str(query_filter) + '%')
            )).all()
        rows = self.controller.dump(patients_to_dump, many=True)

        self._current_patients_cache = rows
        return rows

    def _add_patient(self):
        page = vHandler.patients_form_page_vhandler.PatientFormPageVHandler(self.parent)
        self.parent.load_page(page)

    def _add_patient_with_payload(self):
        data = self._get_current_row_data()
        page = vHandler.patients_form_page_vhandler.PatientFormPageVHandler(self.parent)

        try:
            phone_parts = data.get('phone', ', ').split(', ')
        except AttributeError:
            phone_parts = ['', '']
        phones = []
        for i in range(0, 2):
            try:
                phones.append(phone_parts[i])
            except IndexError:
                phones.append('')
        try:
            birth_date = data.get('birth_date').split('-')
            birth_date = [int(n) for n in birth_date]
        except AttributeError:
            birth_date = [2000, 1, 1]

        page.name_input.setText(data.get('name'))
        page.cpf_input.setText(data.get('cpf'))
        page.rg_input.setText(data.get('rg'))
        page.birth_date_input.setDate(qCore.QDate(y=birth_date[0], m=birth_date[1], d=birth_date[2]))
        page.email_input.setText(data.get('email'))
        page.gender_input.setCurrentIndex(int(data.get('gender')) + 1)
        page.phone1_input.setText(phones[0])
        page.phone2_input.setText(phones[1])

        address_parts = data.get('address').split(', ')
        address = []
        for i in range(0, 7):
            try:
                address.append(address_parts[i])
            except IndexError:
                address.append('')

        page.address_input.setText(address[0])
        page.address_nbr_input.setText(address[1])
        page.complement_input.setText(address[2])
        page.neighb_input.setText(address[3])
        page.city_input.setText(address[4])
        page.estate_input.setText(address[5])
        page.zipcode_input.setText(address[6])

        page._current_patient_cache = data

        self.parent.load_page(page)

    def _search(self):
        filter_txt = self.patient_search_input.text()
        data = self._search_patients(filter_txt)
        self.show_table(data)

    def _open_record(self):
        self.writer = vHandler.RecordWriterVHandler()

