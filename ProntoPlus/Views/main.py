# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 639)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.container_menu = QHBoxLayout()
        self.container_menu.setSpacing(10)
        self.container_menu.setObjectName(u"container_menu")
        self.patients_btn = QPushButton(self.centralwidget)
        self.patients_btn.setObjectName(u"patients_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.patients_btn.sizePolicy().hasHeightForWidth())
        self.patients_btn.setSizePolicy(sizePolicy2)
        self.patients_btn.setMinimumSize(QSize(100, 0))
        self.patients_btn.setMaximumSize(QSize(100, 60))
        self.patients_btn.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/patient.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_btn.setIcon(icon)
        self.patients_btn.setIconSize(QSize(36, 36))

        self.container_menu.addWidget(self.patients_btn)

        self.options_btn = QPushButton(self.centralwidget)
        self.options_btn.setObjectName(u"options_btn")
        sizePolicy2.setHeightForWidth(self.options_btn.sizePolicy().hasHeightForWidth())
        self.options_btn.setSizePolicy(sizePolicy2)
        self.options_btn.setMinimumSize(QSize(100, 0))
        self.options_btn.setMaximumSize(QSize(100, 60))
        self.options_btn.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.options_btn.setIcon(icon1)
        self.options_btn.setIconSize(QSize(36, 36))

        self.container_menu.addWidget(self.options_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.container_menu.addItem(self.horizontalSpacer)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy2.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy2)
        self.exit_btn.setMinimumSize(QSize(100, 0))
        self.exit_btn.setMaximumSize(QSize(100, 60))
        self.exit_btn.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon2)
        self.exit_btn.setIconSize(QSize(36, 36))

        self.container_menu.addWidget(self.exit_btn)

        self.container_menu.setStretch(2, 100)

        self.verticalLayout.addLayout(self.container_menu)

        self.mainArea = QVBoxLayout()
        self.mainArea.setObjectName(u"mainArea")
        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")

        self.mainArea.addWidget(self.main_widget)


        self.verticalLayout.addLayout(self.mainArea)

        self.verticalLayout.setStretch(0, 15)
        self.verticalLayout.setStretch(1, 85)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProntoPlus", None))
        self.patients_btn.setText("")
#if QT_CONFIG(shortcut)
        self.patients_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.options_btn.setText("")
#if QT_CONFIG(shortcut)
        self.options_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.exit_btn.setText("")
#if QT_CONFIG(shortcut)
        self.exit_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

