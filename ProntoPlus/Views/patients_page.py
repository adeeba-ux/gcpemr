# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patients_page.ui'
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

class Ui_patients_page(object):
    def setupUi(self, patients_page):
        if not patients_page.objectName():
            patients_page.setObjectName(u"patients_page")
        patients_page.resize(725, 749)
        patients_page.setStyleSheet(u"")
        self.record_list_action = QAction(patients_page)
        self.record_list_action.setObjectName(u"record_list_action")
        self.verticalLayout = QVBoxLayout(patients_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.container_search_top_h = QHBoxLayout()
        self.container_search_top_h.setObjectName(u"container_search_top_h")
        self.patient_search_input = QLineEdit(patients_page)
        self.patient_search_input.setObjectName(u"patient_search_input")

        self.container_search_top_h.addWidget(self.patient_search_input)

        self.patient_search_btn = QPushButton(patients_page)
        self.patient_search_btn.setObjectName(u"patient_search_btn")
        self.patient_search_btn.setMaximumSize(QSize(50, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patient_search_btn.setIcon(icon)
        self.patient_search_btn.setIconSize(QSize(24, 24))

        self.container_search_top_h.addWidget(self.patient_search_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_search_top_h.addItem(self.horizontalSpacer)

        self.patient_record_add_btn = QPushButton(patients_page)
        self.patient_record_add_btn.setObjectName(u"patient_record_add_btn")
        self.patient_record_add_btn.setEnabled(False)
        self.patient_record_add_btn.setMinimumSize(QSize(40, 30))
        self.patient_record_add_btn.setMaximumSize(QSize(50, 16777215))
        self.patient_record_add_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/information.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patient_record_add_btn.setIcon(icon1)
        self.patient_record_add_btn.setIconSize(QSize(24, 24))
        self.patient_record_add_btn.setAutoDefault(False)
        self.patient_record_add_btn.setFlat(False)

        self.container_search_top_h.addWidget(self.patient_record_add_btn)

        self.patient_edit_btn = QPushButton(patients_page)
        self.patient_edit_btn.setObjectName(u"patient_edit_btn")
        self.patient_edit_btn.setEnabled(False)
        self.patient_edit_btn.setMinimumSize(QSize(40, 30))
        self.patient_edit_btn.setMaximumSize(QSize(50, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patient_edit_btn.setIcon(icon2)
        self.patient_edit_btn.setIconSize(QSize(24, 24))
        self.patient_edit_btn.setAutoDefault(False)
        self.patient_edit_btn.setFlat(False)

        self.container_search_top_h.addWidget(self.patient_edit_btn)

        self.patient_add_btn = QPushButton(patients_page)
        self.patient_add_btn.setObjectName(u"patient_add_btn")
        self.patient_add_btn.setMinimumSize(QSize(0, 30))
        self.patient_add_btn.setMaximumSize(QSize(40, 16777215))
        self.patient_add_btn.setStyleSheet(u"font: 18px;")
        self.patient_add_btn.setIconSize(QSize(24, 24))
        self.patient_add_btn.setAutoDefault(False)
        self.patient_add_btn.setFlat(False)

        self.container_search_top_h.addWidget(self.patient_add_btn)

        self.container_search_top_h.setStretch(0, 50)
        self.container_search_top_h.setStretch(1, 5)
        self.container_search_top_h.setStretch(2, 40)
        self.container_search_top_h.setStretch(3, 5)
        self.container_search_top_h.setStretch(5, 5)

        self.verticalLayout.addLayout(self.container_search_top_h)

        self.container_record_bot_grid = QGridLayout()
        self.container_record_bot_grid.setObjectName(u"container_record_bot_grid")
        self.container_record_bot_grid.setColumnStretch(0, 1)

        self.verticalLayout.addLayout(self.container_record_bot_grid)

        self.patient_table = QTableWidget(patients_page)
        self.patient_table.setObjectName(u"patient_table")
        self.patient_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.patient_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.patient_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.patient_table.setSortingEnabled(True)
        self.patient_table.setColumnCount(0)
        self.patient_table.horizontalHeader().setMinimumSectionSize(100)
        self.patient_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.patient_table)


        self.retranslateUi(patients_page)

        self.patient_record_add_btn.setDefault(False)
        self.patient_edit_btn.setDefault(False)
        self.patient_add_btn.setDefault(False)


        QMetaObject.connectSlotsByName(patients_page)
    # setupUi

    def retranslateUi(self, patients_page):
        patients_page.setWindowTitle(QCoreApplication.translate("patients_page", u"patientsPage", None))
        self.record_list_action.setText(QCoreApplication.translate("patients_page", u"Listar Prontu\u00e1rios", None))
#if QT_CONFIG(tooltip)
        self.record_list_action.setToolTip(QCoreApplication.translate("patients_page", u"Listar prontu\u00e1rios para esse usu\u00e1rio", None))
#endif // QT_CONFIG(tooltip)
        self.patient_search_btn.setText("")
#if QT_CONFIG(shortcut)
        self.patient_search_btn.setShortcut(QCoreApplication.translate("patients_page", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.patient_record_add_btn.setText("")
        self.patient_edit_btn.setText("")
        self.patient_add_btn.setText(QCoreApplication.translate("patients_page", u"+", None))
    # retranslateUi

