# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(272, 205)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(272, 205))
        Dialog.setMaximumSize(QSize(272, 205))
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.container_v = QVBoxLayout()
        self.container_v.setObjectName(u"container_v")
        self.title_lbl = QLabel(Dialog)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setStyleSheet(u"font: 75 14pt \"DejaVu Sans\";")
        self.title_lbl.setAlignment(Qt.AlignCenter)

        self.container_v.addWidget(self.title_lbl)

        self.container_user_h = QHBoxLayout()
        self.container_user_h.setObjectName(u"container_user_h")
        self.user_lbl = QLabel(Dialog)
        self.user_lbl.setObjectName(u"user_lbl")
        self.user_lbl.setStyleSheet(u"font: 10pt \"Arial\";")
        self.user_lbl.setAlignment(Qt.AlignCenter)

        self.container_user_h.addWidget(self.user_lbl)

        self.user_input = QLineEdit(Dialog)
        self.user_input.setObjectName(u"user_input")

        self.container_user_h.addWidget(self.user_input)

        self.container_user_h.setStretch(0, 25)
        self.container_user_h.setStretch(1, 75)

        self.container_v.addLayout(self.container_user_h)

        self.container_pass_h = QHBoxLayout()
        self.container_pass_h.setObjectName(u"container_pass_h")
        self.pass_lbl = QLabel(Dialog)
        self.pass_lbl.setObjectName(u"pass_lbl")
        self.pass_lbl.setAlignment(Qt.AlignCenter)

        self.container_pass_h.addWidget(self.pass_lbl)

        self.pass_input = QLineEdit(Dialog)
        self.pass_input.setObjectName(u"pass_input")

        self.container_pass_h.addWidget(self.pass_input)

        self.container_pass_h.setStretch(0, 25)
        self.container_pass_h.setStretch(1, 75)

        self.container_v.addLayout(self.container_pass_h)


        self.verticalLayout.addLayout(self.container_v)

        self.login_dialog_btn = QDialogButtonBox(Dialog)
        self.login_dialog_btn.setObjectName(u"login_dialog_btn")
        self.login_dialog_btn.setOrientation(Qt.Horizontal)
        self.login_dialog_btn.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.login_dialog_btn)


        self.retranslateUi(Dialog)
        self.login_dialog_btn.accepted.connect(Dialog.accept)
        self.login_dialog_btn.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title_lbl.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.user_lbl.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.pass_lbl.setText(QCoreApplication.translate("Dialog", u"Senha:", None))
    # retranslateUi

