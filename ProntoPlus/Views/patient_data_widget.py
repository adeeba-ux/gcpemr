# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_data_widget.ui'
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


class Ui_patient_data(object):
    def setupUi(self, patient_data):
        if not patient_data.objectName():
            patient_data.setObjectName(u"patient_data")
        patient_data.resize(640, 134)
        self.gridLayout = QGridLayout(patient_data)
        self.gridLayout.setObjectName(u"gridLayout")
        self.patient_lbl = QLabel(patient_data)
        self.patient_lbl.setObjectName(u"patient_lbl")
        self.patient_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.patient_lbl, 1, 0, 1, 1)

        self.gender_lbl = QLabel(patient_data)
        self.gender_lbl.setObjectName(u"gender_lbl")
        self.gender_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.gender_lbl, 4, 0, 1, 1)

        self.date_lbl = QLabel(patient_data)
        self.date_lbl.setObjectName(u"date_lbl")
        self.date_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.date_lbl, 0, 0, 1, 1)

        self.patient_name_output = QLabel(patient_data)
        self.patient_name_output.setObjectName(u"patient_name_output")

        self.gridLayout.addWidget(self.patient_name_output, 1, 1, 1, 1)

        self.age_output = QLabel(patient_data)
        self.age_output.setObjectName(u"age_output")

        self.gridLayout.addWidget(self.age_output, 3, 1, 1, 1)

        self.gender_output = QLabel(patient_data)
        self.gender_output.setObjectName(u"gender_output")

        self.gridLayout.addWidget(self.gender_output, 4, 1, 1, 1)

        self.age_lbl = QLabel(patient_data)
        self.age_lbl.setObjectName(u"age_lbl")
        self.age_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.age_lbl, 3, 0, 1, 1)

        self.date_output = QLabel(patient_data)
        self.date_output.setObjectName(u"date_output")

        self.gridLayout.addWidget(self.date_output, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(patient_data)

        QMetaObject.connectSlotsByName(patient_data)
    # setupUi

    def retranslateUi(self, patient_data):
        patient_data.setWindowTitle(QCoreApplication.translate("patient_data", u"Form", None))
        self.patient_lbl.setText(QCoreApplication.translate("patient_data", u"Paciente:", None))
        self.gender_lbl.setText(QCoreApplication.translate("patient_data", u"Sexo:", None))
        self.date_lbl.setText(QCoreApplication.translate("patient_data", u"Data:", None))
        self.patient_name_output.setText(QCoreApplication.translate("patient_data", u"PATIENT_NAME_LBL", None))
        self.age_output.setText(QCoreApplication.translate("patient_data", u"AGE_LBL", None))
        self.gender_output.setText(QCoreApplication.translate("patient_data", u"GENDER_LBL", None))
        self.age_lbl.setText(QCoreApplication.translate("patient_data", u"Idade:", None))
        self.date_output.setText(QCoreApplication.translate("patient_data", u"DATE_LBL", None))
    # retranslateUi

