# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'records_page.ui'
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


class Ui_records_page(object):
    def setupUi(self, records_page):
        if not records_page.objectName():
            records_page.setObjectName(u"records_page")
        records_page.resize(909, 841)
        self.verticalLayout = QVBoxLayout(records_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.patient_name_output = QLabel(records_page)
        self.patient_name_output.setObjectName(u"patient_name_output")
        self.patient_name_output.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.patient_name_output)

        self.container_header_h = QHBoxLayout()
        self.container_header_h.setObjectName(u"container_header_h")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_header_h.addItem(self.horizontalSpacer)

        self.container_header_form = QFormLayout()
        self.container_header_form.setObjectName(u"container_header_form")
        self.container_header_form.setSizeConstraint(QLayout.SetFixedSize)
        self.container_header_form.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.container_header_form.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.container_header_form.setHorizontalSpacing(10)
        self.age_lbl = QLabel(records_page)
        self.age_lbl.setObjectName(u"age_lbl")

        self.container_header_form.setWidget(0, QFormLayout.LabelRole, self.age_lbl)

        self.age_output = QLabel(records_page)
        self.age_output.setObjectName(u"age_output")
        self.age_output.setMinimumSize(QSize(100, 0))
        self.age_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.container_header_form.setWidget(0, QFormLayout.FieldRole, self.age_output)

        self.created_output = QLabel(records_page)
        self.created_output.setObjectName(u"created_output")
        self.created_output.setMinimumSize(QSize(200, 0))
        self.created_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.container_header_form.setWidget(1, QFormLayout.FieldRole, self.created_output)

        self.created_lbl = QLabel(records_page)
        self.created_lbl.setObjectName(u"created_lbl")
        self.created_lbl.setMinimumSize(QSize(200, 0))
        self.created_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_header_form.setWidget(1, QFormLayout.LabelRole, self.created_lbl)

        self.total_records_lbl = QLabel(records_page)
        self.total_records_lbl.setObjectName(u"total_records_lbl")
        self.total_records_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.container_header_form.setWidget(2, QFormLayout.LabelRole, self.total_records_lbl)

        self.total_records_output = QLabel(records_page)
        self.total_records_output.setObjectName(u"total_records_output")
        self.total_records_output.setMinimumSize(QSize(200, 0))
        self.total_records_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.container_header_form.setWidget(2, QFormLayout.FieldRole, self.total_records_output)


        self.container_header_h.addLayout(self.container_header_form)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_header_h.addItem(self.horizontalSpacer_2)

        self.container_header_h.setStretch(0, 1)
        self.container_header_h.setStretch(2, 1)

        self.verticalLayout.addLayout(self.container_header_h)

        self.container_btn_h = QHBoxLayout()
        self.container_btn_h.setObjectName(u"container_btn_h")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_btn_h.addItem(self.horizontalSpacer_6)

        self.record_add_btn = QPushButton(records_page)
        self.record_add_btn.setObjectName(u"record_add_btn")

        self.container_btn_h.addWidget(self.record_add_btn)

        self.redcord_edit_btn = QPushButton(records_page)
        self.redcord_edit_btn.setObjectName(u"redcord_edit_btn")
        self.redcord_edit_btn.setEnabled(False)

        self.container_btn_h.addWidget(self.redcord_edit_btn)

        self.record_delete_btn = QPushButton(records_page)
        self.record_delete_btn.setObjectName(u"record_delete_btn")
        self.record_delete_btn.setEnabled(False)

        self.container_btn_h.addWidget(self.record_delete_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_btn_h.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.container_btn_h)

        self.container_table_h = QHBoxLayout()
        self.container_table_h.setObjectName(u"container_table_h")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_table_h.addItem(self.horizontalSpacer_4)

        self.record_table = QTableWidget(records_page)
        self.record_table.setObjectName(u"record_table")
        self.record_table.setMinimumSize(QSize(500, 0))

        self.container_table_h.addWidget(self.record_table)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_table_h.addItem(self.horizontalSpacer_3)

        self.container_table_h.setStretch(0, 1)
        self.container_table_h.setStretch(2, 1)

        self.verticalLayout.addLayout(self.container_table_h)


        self.retranslateUi(records_page)

        QMetaObject.connectSlotsByName(records_page)
    # setupUi

    def retranslateUi(self, records_page):
        records_page.setWindowTitle("")
        self.patient_name_output.setText(QCoreApplication.translate("records_page", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">PATIENT_NAME</span></p></body></html>", None))
        self.age_lbl.setText(QCoreApplication.translate("records_page", u"Idade", None))
        self.age_output.setText(QCoreApplication.translate("records_page", u"REF", None))
        self.created_output.setText(QCoreApplication.translate("records_page", u"REF", None))
        self.created_lbl.setText(QCoreApplication.translate("records_page", u"Criado em", None))
        self.total_records_lbl.setText(QCoreApplication.translate("records_page", u"Prontu\u00e1rios", None))
        self.total_records_output.setText(QCoreApplication.translate("records_page", u"REF", None))
        self.record_add_btn.setText(QCoreApplication.translate("records_page", u"Adicionar", None))
        self.redcord_edit_btn.setText(QCoreApplication.translate("records_page", u"Editar", None))
        self.record_delete_btn.setText(QCoreApplication.translate("records_page", u"Apagar", None))
    # retranslateUi

