# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patients_form_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import ProntoPlus.Views.assets_rc

class Ui_patients_form_page(object):
    def setupUi(self, patients_form_page):
        if not patients_form_page.objectName():
            patients_form_page.setObjectName(u"patients_form_page")
        patients_form_page.resize(990, 706)
        self.verticalLayout = QVBoxLayout(patients_form_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.general_lbl = QLabel(patients_form_page)
        self.general_lbl.setObjectName(u"general_lbl")
        self.general_lbl.setStyleSheet(u"font: 18px bold;")

        self.verticalLayout.addWidget(self.general_lbl)

        self.container_general_grid = QGridLayout()
        self.container_general_grid.setObjectName(u"container_general_grid")
        self.cpf_input = QLineEdit(patients_form_page)
        self.cpf_input.setObjectName(u"cpf_input")

        self.container_general_grid.addWidget(self.cpf_input, 4, 1, 1, 1)

        self.gender_input = QComboBox(patients_form_page)
        self.gender_input.addItem("")
        self.gender_input.addItem("")
        self.gender_input.addItem("")
        self.gender_input.addItem("")
        self.gender_input.setObjectName(u"gender_input")

        self.container_general_grid.addWidget(self.gender_input, 1, 1, 1, 1)

        self.phone2_lbl = QLabel(patients_form_page)
        self.phone2_lbl.setObjectName(u"phone2_lbl")
        self.phone2_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.phone2_lbl, 5, 2, 1, 1)

        self.name_input = QLineEdit(patients_form_page)
        self.name_input.setObjectName(u"name_input")

        self.container_general_grid.addWidget(self.name_input, 0, 1, 1, 1)

        self.phone1_input = QLineEdit(patients_form_page)
        self.phone1_input.setObjectName(u"phone1_input")

        self.container_general_grid.addWidget(self.phone1_input, 5, 1, 1, 1)

        self.rg_input = QLineEdit(patients_form_page)
        self.rg_input.setObjectName(u"rg_input")

        self.container_general_grid.addWidget(self.rg_input, 4, 3, 1, 1)

        self.name_lbl = QLabel(patients_form_page)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.name_lbl, 0, 0, 1, 1)

        self.cpf_lbl = QLabel(patients_form_page)
        self.cpf_lbl.setObjectName(u"cpf_lbl")
        self.cpf_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.cpf_lbl, 4, 0, 1, 1)

        self.email_input = QLineEdit(patients_form_page)
        self.email_input.setObjectName(u"email_input")

        self.container_general_grid.addWidget(self.email_input, 3, 1, 1, 1)

        self.gender_lbl = QLabel(patients_form_page)
        self.gender_lbl.setObjectName(u"gender_lbl")
        self.gender_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.gender_lbl, 1, 0, 1, 1)

        self.birth_date_input = QDateEdit(patients_form_page)
        self.birth_date_input.setObjectName(u"birth_date_input")
        self.birth_date_input.setEnabled(False)
        self.birth_date_input.setMinimumDateTime(QDateTime(QDate(1901, 1, 1), QTime(0, 0, 0)))
        self.birth_date_input.setCalendarPopup(True)

        self.container_general_grid.addWidget(self.birth_date_input, 2, 1, 1, 1)

        self.rg_lbl = QLabel(patients_form_page)
        self.rg_lbl.setObjectName(u"rg_lbl")
        self.rg_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.rg_lbl, 4, 2, 1, 1)

        self.phone2_input = QLineEdit(patients_form_page)
        self.phone2_input.setObjectName(u"phone2_input")

        self.container_general_grid.addWidget(self.phone2_input, 5, 3, 1, 1)

        self.birth_date_null_check = QCheckBox(patients_form_page)
        self.birth_date_null_check.setObjectName(u"birth_date_null_check")
        self.birth_date_null_check.setChecked(True)
        self.birth_date_null_check.setTristate(False)

        self.container_general_grid.addWidget(self.birth_date_null_check, 2, 2, 1, 1)

        self.email_lbl = QLabel(patients_form_page)
        self.email_lbl.setObjectName(u"email_lbl")
        self.email_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.email_lbl, 3, 0, 1, 1)

        self.birth_date_lbl = QLabel(patients_form_page)
        self.birth_date_lbl.setObjectName(u"birth_date_lbl")
        self.birth_date_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.birth_date_lbl, 2, 0, 1, 1)

        self.phone1_lbl = QLabel(patients_form_page)
        self.phone1_lbl.setObjectName(u"phone1_lbl")
        self.phone1_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_general_grid.addWidget(self.phone1_lbl, 5, 0, 1, 1)

        self.container_general_grid.setColumnStretch(1, 2)
        self.container_general_grid.setColumnStretch(3, 1)

        self.verticalLayout.addLayout(self.container_general_grid)

        self.address_lbl_2 = QLabel(patients_form_page)
        self.address_lbl_2.setObjectName(u"address_lbl_2")
        self.address_lbl_2.setStyleSheet(u"font: 18px bold;")

        self.verticalLayout.addWidget(self.address_lbl_2)

        self.container_address_grid = QGridLayout()
        self.container_address_grid.setObjectName(u"container_address_grid")
        self.address_input = QLineEdit(patients_form_page)
        self.address_input.setObjectName(u"address_input")

        self.container_address_grid.addWidget(self.address_input, 1, 1, 1, 1)

        self.neighb_input = QLineEdit(patients_form_page)
        self.neighb_input.setObjectName(u"neighb_input")

        self.container_address_grid.addWidget(self.neighb_input, 2, 3, 1, 1)

        self.neighb_lbl = QLabel(patients_form_page)
        self.neighb_lbl.setObjectName(u"neighb_lbl")
        self.neighb_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_address_grid.addWidget(self.neighb_lbl, 2, 2, 1, 1)

        self.address_nbr_input = QLineEdit(patients_form_page)
        self.address_nbr_input.setObjectName(u"address_nbr_input")

        self.container_address_grid.addWidget(self.address_nbr_input, 1, 3, 1, 1)

        self.complement_input = QLineEdit(patients_form_page)
        self.complement_input.setObjectName(u"complement_input")

        self.container_address_grid.addWidget(self.complement_input, 2, 1, 1, 1)

        self.estate_input = QLineEdit(patients_form_page)
        self.estate_input.setObjectName(u"estate_input")

        self.container_address_grid.addWidget(self.estate_input, 3, 3, 1, 1)

        self.complement_lbl = QLabel(patients_form_page)
        self.complement_lbl.setObjectName(u"complement_lbl")
        self.complement_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_address_grid.addWidget(self.complement_lbl, 2, 0, 1, 1)

        self.zipcode_lbl = QLabel(patients_form_page)
        self.zipcode_lbl.setObjectName(u"zipcode_lbl")
        self.zipcode_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_address_grid.addWidget(self.zipcode_lbl, 0, 0, 1, 1)

        self.address_nbr_lbl = QLabel(patients_form_page)
        self.address_nbr_lbl.setObjectName(u"address_nbr_lbl")
        self.address_nbr_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_address_grid.addWidget(self.address_nbr_lbl, 1, 2, 1, 1)

        self.zipcode_input = QLineEdit(patients_form_page)
        self.zipcode_input.setObjectName(u"zipcode_input")

        self.container_address_grid.addWidget(self.zipcode_input, 0, 1, 1, 1)

        self.city_lbl = QLabel(patients_form_page)
        self.city_lbl.setObjectName(u"city_lbl")
        self.city_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_address_grid.addWidget(self.city_lbl, 3, 0, 1, 1)

        self.address_lbl = QLabel(patients_form_page)
        self.address_lbl.setObjectName(u"address_lbl")
        self.address_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_address_grid.addWidget(self.address_lbl, 1, 0, 1, 1)

        self.estate_lbl = QLabel(patients_form_page)
        self.estate_lbl.setObjectName(u"estate_lbl")
        self.estate_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_address_grid.addWidget(self.estate_lbl, 3, 2, 1, 1)

        self.city_input = QLineEdit(patients_form_page)
        self.city_input.setObjectName(u"city_input")

        self.container_address_grid.addWidget(self.city_input, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.container_address_grid)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.container_btns = QSplitter(patients_form_page)
        self.container_btns.setObjectName(u"container_btns")
        self.container_btns.setOrientation(Qt.Horizontal)
        self.save_btn = QPushButton(self.container_btns)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMaximumSize(QSize(200, 50))
        icon = QIcon()
        icon.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon)
        self.save_btn.setIconSize(QSize(36, 36))
        self.container_btns.addWidget(self.save_btn)
        self.cancel_btn = QPushButton(self.container_btns)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMaximumSize(QSize(200, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_btn.setIcon(icon1)
        self.cancel_btn.setIconSize(QSize(36, 36))
        self.container_btns.addWidget(self.cancel_btn)

        self.verticalLayout.addWidget(self.container_btns)

        self.verticalLayout.setStretch(1, 15)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 15)
        QWidget.setTabOrder(self.name_input, self.gender_input)
        QWidget.setTabOrder(self.gender_input, self.birth_date_input)
        QWidget.setTabOrder(self.birth_date_input, self.birth_date_null_check)
        QWidget.setTabOrder(self.birth_date_null_check, self.email_input)
        QWidget.setTabOrder(self.email_input, self.cpf_input)
        QWidget.setTabOrder(self.cpf_input, self.rg_input)
        QWidget.setTabOrder(self.rg_input, self.phone1_input)
        QWidget.setTabOrder(self.phone1_input, self.phone2_input)
        QWidget.setTabOrder(self.phone2_input, self.zipcode_input)
        QWidget.setTabOrder(self.zipcode_input, self.address_input)
        QWidget.setTabOrder(self.address_input, self.address_nbr_input)
        QWidget.setTabOrder(self.address_nbr_input, self.complement_input)
        QWidget.setTabOrder(self.complement_input, self.neighb_input)
        QWidget.setTabOrder(self.neighb_input, self.city_input)
        QWidget.setTabOrder(self.city_input, self.estate_input)
        QWidget.setTabOrder(self.estate_input, self.save_btn)
        QWidget.setTabOrder(self.save_btn, self.cancel_btn)

        self.retranslateUi(patients_form_page)

        QMetaObject.connectSlotsByName(patients_form_page)
    # setupUi

    def retranslateUi(self, patients_form_page):
        patients_form_page.setWindowTitle(QCoreApplication.translate("patients_form_page", u"Form", None))
        self.general_lbl.setText(QCoreApplication.translate("patients_form_page", u"Geral", None))
        self.cpf_input.setInputMask(QCoreApplication.translate("patients_form_page", u"000.000.000-00;_", None))
        self.gender_input.setItemText(0, "")
        self.gender_input.setItemText(1, QCoreApplication.translate("patients_form_page", u"Masculino", None))
        self.gender_input.setItemText(2, QCoreApplication.translate("patients_form_page", u"Feminino", None))
        self.gender_input.setItemText(3, "")

        self.gender_input.setCurrentText("")
        self.phone2_lbl.setText(QCoreApplication.translate("patients_form_page", u"Telefone 2", None))
        self.phone1_input.setInputMask(QCoreApplication.translate("patients_form_page", u"(99)99999-9999;_", None))
        self.rg_input.setInputMask("")
        self.name_lbl.setText(QCoreApplication.translate("patients_form_page", u"Nome", None))
        self.cpf_lbl.setText(QCoreApplication.translate("patients_form_page", u"CPF", None))
        self.email_input.setInputMask("")
        self.gender_lbl.setText(QCoreApplication.translate("patients_form_page", u"Sexo", None))
        self.birth_date_input.setDisplayFormat(QCoreApplication.translate("patients_form_page", u"dd/MM/yyyy", None))
        self.rg_lbl.setText(QCoreApplication.translate("patients_form_page", u"RG", None))
        self.phone2_input.setInputMask(QCoreApplication.translate("patients_form_page", u"(99)99999-9999;_", None))
        self.birth_date_null_check.setText(QCoreApplication.translate("patients_form_page", u"N\u00e3o informar", None))
        self.email_lbl.setText(QCoreApplication.translate("patients_form_page", u"E-mail", None))
        self.birth_date_lbl.setText(QCoreApplication.translate("patients_form_page", u"Data de nasc.", None))
        self.phone1_lbl.setText(QCoreApplication.translate("patients_form_page", u"Telefone", None))
        self.address_lbl_2.setText(QCoreApplication.translate("patients_form_page", u"Endere\u00e7o", None))
        self.neighb_lbl.setText(QCoreApplication.translate("patients_form_page", u"Bairro", None))
        self.complement_lbl.setText(QCoreApplication.translate("patients_form_page", u"Complemento", None))
        self.zipcode_lbl.setText(QCoreApplication.translate("patients_form_page", u"CEP", None))
        self.address_nbr_lbl.setText(QCoreApplication.translate("patients_form_page", u"N\u00famero", None))
        self.zipcode_input.setInputMask(QCoreApplication.translate("patients_form_page", u"99999-999;_", None))
        self.city_lbl.setText(QCoreApplication.translate("patients_form_page", u"Complemento", None))
        self.address_lbl.setText(QCoreApplication.translate("patients_form_page", u"Endere\u00e7o", None))
        self.estate_lbl.setText(QCoreApplication.translate("patients_form_page", u"Estado", None))
        self.save_btn.setText("")
        self.cancel_btn.setText("")
    # retranslateUi

