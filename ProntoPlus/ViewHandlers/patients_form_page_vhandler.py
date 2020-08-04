import ProntoPlus.Views as views
import ProntoPlus.Controllers as Ctrls
import ProntoPlus.ViewHandlers as vHandlers

import PySide2.QtWidgets as qtW
import PySide2.QtCore as qCore
import uuid
import datetime as dt


class PatientFormPageVHandler(views.patients_form_page.Ui_patients_form_page, qtW.QWidget):

    def __init__(self, parent: qtW.QMainWindow = None, patient: Ctrls.PatientCtrl.CTRLCLASS = None):
        super().__init__()
        self.parent = parent
        self.controller = Ctrls.init_patient_ctrl()
        if patient is None:
            new_patient_data = {
                'id': uuid.uuid4(),
                'tenant': self.parent.TENANT,
                'name': '',
                'cpf': '',
                'created_date': dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
            self.patient = self.controller.load(new_patient_data)
        else:
            self.patient = patient
        self.patient_ctrl = Ctrls.init_patient_ctrl()
        self.setupUi(self)

        self.setup_buttons()

    def setup_buttons(self):
        self.save_btn.clicked.connect(self._save)
        self.cancel_btn.clicked.connect(self._cancel)

    def _save(self):
        self.patient.name = self.name_input.text()
        self.patient.rg = self.rg_input.text()
        self.patient.cpf = self.cpf_input.text()
        self.patient.gender = self.patient.Gender(self.gender_input.currentIndex() - 1)
        if self.birth_date_input.isEnabled():
            self.patient.birth_date = self.birth_date_input.date()
        self.patient.email = self.email_input.text()
        self.patient.phone = ', '.join([self.phone1_input.text(), self.phone2_input.text()])

        adr_street = self.address_input.text()
        adr_number = self.address_nbr_input.text()
        adr_complement = self.complement_input.text()
        adr_neighborhood = self.neighb_input.text()
        adr_city = self.city_input.text()
        adr_estate = self.estate_input.text()
        adr_zip = self.zipcode_input.text()

        address_parts = [adr_street, adr_number, adr_complement, adr_neighborhood, adr_city, adr_estate, adr_zip]
        self.patient.address = ', '.join(address_parts)

        self.patient.last_modified_date = dt.datetime.now()

        self.controller.add(self.patient)

        self._load_patient_page()

    def _cancel(self):
        self._load_patient_page()

    def _load_patient_page(self):
        page = vHandlers.PatientsPageVHandler(self.parent)
        self.parent.load_page(page)

    def setup_patient_data(self):
        data = self.patient
        try:
            phone_parts = data.phone.split(', ')
        except AttributeError:
            phone_parts = ['', '']
        phones = []
        for i in range(0, 2):
            try:
                phones.append(phone_parts[i])
            except IndexError:
                phones.append('')
        try:
            birth_date = data.birth_date.split('-')
            birth_date = [int(n) for n in birth_date]
        except AttributeError:
            birth_date = [2000, 1, 1]

        self.name_input.setText(data.name)
        self.cpf_input.setText(data.cpf)
        self.rg_input.setText(data.rg)
        self.birth_date_input.setDate(qCore.QDate(birth_date[0], birth_date[1], birth_date[2]))
        self.email_input.setText(data.email)
        self.gender_input.setCurrentIndex(data.gender.value+1)
        self.phone1_input.setText(phones[0])
        self.phone2_input.setText(phones[1])

        address_parts = data.address.split(', ')
        address = []
        for i in range(0, 7):
            try:
                address.append(address_parts[i])
            except IndexError:
                address.append('')

        self.address_input.setText(address[0])
        self.address_nbr_input.setText(address[1])
        self.complement_input.setText(address[2])
        self.neighb_input.setText(address[3])
        self.city_input.setText(address[4])
        self.estate_input.setText(address[5])
        self.zipcode_input.setText(address[6])
