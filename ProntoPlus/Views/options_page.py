# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_page.ui'
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


class Ui_options_page(object):
    def setupUi(self, options_page):
        if not options_page.objectName():
            options_page.setObjectName(u"options_page")
        options_page.resize(640, 480)
        self.verticalLayout = QVBoxLayout(options_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.connstring_lbl = QLabel(options_page)
        self.connstring_lbl.setObjectName(u"connstring_lbl")

        self.gridLayout.addWidget(self.connstring_lbl, 0, 0, 1, 1)

        self.cancel_btn = QPushButton(options_page)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout.addWidget(self.cancel_btn, 1, 2, 1, 1)

        self.save_btn = QPushButton(options_page)
        self.save_btn.setObjectName(u"save_btn")

        self.gridLayout.addWidget(self.save_btn, 1, 3, 1, 1)

        self.connstring_input = QLineEdit(options_page)
        self.connstring_input.setObjectName(u"connstring_input")

        self.gridLayout.addWidget(self.connstring_input, 0, 1, 1, 2)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(options_page)

        QMetaObject.connectSlotsByName(options_page)
    # setupUi

    def retranslateUi(self, options_page):
        options_page.setWindowTitle(QCoreApplication.translate("options_page", u"Op\u00e7\u00f5es", None))
        self.connstring_lbl.setText(QCoreApplication.translate("options_page", u"String de conex\u00e3o do banco de dados:", None))
        self.cancel_btn.setText(QCoreApplication.translate("options_page", u"Cancelar", None))
        self.save_btn.setText(QCoreApplication.translate("options_page", u"Salvar", None))
    # retranslateUi

