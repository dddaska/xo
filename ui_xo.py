# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xo.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(509, 597)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 451, 551))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 130))
        self.label.setStyleSheet(u"color: #C13D3D;\n"
"font-family: \"Comic Sans MS\", \"Caveat\", \"Segoe Print\", cursive;\n"
"font-size:36px;\n"
"font-weight: bold;\n"
"padding:20px;")

        self.verticalLayout.addWidget(self.label)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"QWidget{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent ;\n"
"	border: 2px solid #C13D3D;\n"
"    border-radius: 0;\n"
"	color: #C13D3D;\n"
"	font-family: \"Comic Sans MS\", \"Segoe Print\", cursive;\n"
"	font-size: 36px;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(193, 61, 61, 0.08);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(193, 61, 61, 0.15);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.gridLayoutWidget = QWidget(self.widget1)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 431, 381))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn9 = QPushButton(self.gridLayoutWidget)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(70, 70))
        self.btn9.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)

        self.btn8 = QPushButton(self.gridLayoutWidget)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(70, 70))
        self.btn8.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)

        self.btn1 = QPushButton(self.gridLayoutWidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(70, 70))
        self.btn1.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)

        self.btn7 = QPushButton(self.gridLayoutWidget)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(70, 70))
        self.btn7.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)

        self.btn4 = QPushButton(self.gridLayoutWidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(70, 70))
        self.btn4.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn2 = QPushButton(self.gridLayoutWidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(70, 70))
        self.btn2.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)

        self.btn3 = QPushButton(self.gridLayoutWidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(70, 70))
        self.btn3.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)

        self.btn6 = QPushButton(self.gridLayoutWidget)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(70, 70))
        self.btn6.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        self.btn5 = QPushButton(self.gridLayoutWidget)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(70, 70))
        self.btn5.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget1)

        self.resetBtn = QPushButton(self.widget)
        self.resetBtn.setObjectName(u"resetBtn")

        self.verticalLayout.addWidget(self.resetBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.resetBtn.raise_()
        self.label.raise_()
        self.widget1.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0435\u0441\u0442\u0438\u043a\u0438-\u041d\u043e\u043b\u0438\u043a\u0438", None))
        self.btn9.setText("")
        self.btn8.setText("")
        self.btn1.setText("")
        self.btn7.setText("")
        self.btn4.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn6.setText("")
        self.btn5.setText("")
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0441\u043d\u0430\u0447\u0430\u043b\u0430", None))
    # retranslateUi

