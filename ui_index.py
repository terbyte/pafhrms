# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1518, 1316)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_20 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_20 = QFrame(self.centralwidget)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_20)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_21)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.top_widget = QWidget(self.frame_21)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.top_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.top_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/newPrefix/icon/Logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.top_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font-size:20px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(707, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_11 = QPushButton(self.top_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon = QIcon()
        icon.addFile(u":/ /icon/PersonalRecords.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_24 = QPushButton(self.top_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setIcon(icon)
        self.pushButton_24.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_24)


        self.verticalLayout_22.addWidget(self.top_widget)


        self.gridLayout_13.addWidget(self.frame_21, 0, 0, 1, 2)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.main_widget = QWidget(self.frame_23)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"background-color:#f8f9fa;\n"
"\n"
"color:Black")
        self.verticalLayout_24 = QVBoxLayout(self.main_widget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.personnel_records_page = QWidget()
        self.personnel_records_page.setObjectName(u"personnel_records_page")
        self.verticalLayout_26 = QVBoxLayout(self.personnel_records_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_4 = QLabel(self.personnel_records_page)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color:white;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_4)

        self.frame = QFrame(self.personnel_records_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frstName_txtbx = QLineEdit(self.frame)
        self.frstName_txtbx.setObjectName(u"frstName_txtbx")

        self.gridLayout.addWidget(self.frstName_txtbx, 1, 1, 1, 1)

        self.mddlName_txtbx = QLineEdit(self.frame)
        self.mddlName_txtbx.setObjectName(u"mddlName_txtbx")

        self.gridLayout.addWidget(self.mddlName_txtbx, 1, 2, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color:black")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 2, 1, 1)

        self.lastName_txtbx = QLineEdit(self.frame)
        self.lastName_txtbx.setObjectName(u"lastName_txtbx")

        self.gridLayout.addWidget(self.lastName_txtbx, 1, 0, 1, 1)

        self.suffix_txtbx = QLineEdit(self.frame)
        self.suffix_txtbx.setObjectName(u"suffix_txtbx")
        self.suffix_txtbx.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.suffix_txtbx, 1, 3, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color:black")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 0, 3, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color:black")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 0, 1, 1, 1)


        self.verticalLayout_26.addWidget(self.frame)

        self.frame_2 = QFrame(self.personnel_records_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rank_txtbx = QLineEdit(self.frame_2)
        self.rank_txtbx.setObjectName(u"rank_txtbx")
        self.rank_txtbx.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.rank_txtbx, 3, 1, 1, 1)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color:black")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.sex_txtbx = QLineEdit(self.frame_2)
        self.sex_txtbx.setObjectName(u"sex_txtbx")

        self.gridLayout_2.addWidget(self.sex_txtbx, 3, 3, 1, 1)

        self.unit_txtbx = QLineEdit(self.frame_2)
        self.unit_txtbx.setObjectName(u"unit_txtbx")

        self.gridLayout_2.addWidget(self.unit_txtbx, 3, 4, 1, 1)

        self.afpsn_txtbx = QLineEdit(self.frame_2)
        self.afpsn_txtbx.setObjectName(u"afpsn_txtbx")
        self.afpsn_txtbx.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.afpsn_txtbx, 3, 0, 1, 1)

        self.clssfication_txtbx = QLineEdit(self.frame_2)
        self.clssfication_txtbx.setObjectName(u"clssfication_txtbx")

        self.gridLayout_2.addWidget(self.clssfication_txtbx, 3, 2, 1, 1)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"color:black")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_21, 0, 4, 1, 1)

        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"color:black")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_26, 0, 3, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"color:black")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_18, 0, 1, 1, 1)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color:black")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_19, 0, 2, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_2)

        self.label_27 = QLabel(self.personnel_records_page)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color:white;")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_27)

        self.tableWidget_2 = QTableWidget(self.personnel_records_page)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(193)

        self.verticalLayout_26.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.personnel_records_page)
        self.placementpage_enlist_page = QWidget()
        self.placementpage_enlist_page.setObjectName(u"placementpage_enlist_page")
        self.frame_12 = QFrame(self.placementpage_enlist_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(20, 20, 1111, 401))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_12)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_31 = QLabel(self.frame_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color :White;")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_31)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_56 = QLabel(self.frame_15)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_18.addWidget(self.label_56)

        self.label_32 = QLabel(self.frame_15)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_18.addWidget(self.label_32)

        self.label_53 = QLabel(self.frame_15)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_18.addWidget(self.label_53)

        self.label_54 = QLabel(self.frame_15)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_18.addWidget(self.label_54)

        self.label_55 = QLabel(self.frame_15)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_18.addWidget(self.label_55)


        self.horizontalLayout_3.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.textEdit_7 = QTextEdit(self.frame_14)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_14.addWidget(self.textEdit_7)

        self.textEdit_10 = QTextEdit(self.frame_14)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_14.addWidget(self.textEdit_10)

        self.comboBox = QComboBox(self.frame_14)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_14.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.frame_14)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_14.addWidget(self.comboBox_2)

        self.textEdit_8 = QTextEdit(self.frame_14)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_14.addWidget(self.textEdit_8)


        self.horizontalLayout_3.addWidget(self.frame_14)


        self.verticalLayout_25.addWidget(self.frame_13)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_145 = QLabel(self.frame_16)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font1)
        self.label_145.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.horizontalLayout_4.addWidget(self.label_145)

        self.textEdit_28 = QTextEdit(self.frame_16)
        self.textEdit_28.setObjectName(u"textEdit_28")
        self.textEdit_28.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.textEdit_28)

        self.pushButton_9 = QPushButton(self.frame_16)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_25.addWidget(self.frame_16)

        self.pushButton_2 = QPushButton(self.frame_12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font2 = QFont()
        font2.setPointSize(20)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color:white;")

        self.verticalLayout_25.addWidget(self.pushButton_2)

        self.stackedWidget.addWidget(self.placementpage_enlist_page)
        self.Placement_page_officer_page = QWidget()
        self.Placement_page_officer_page.setObjectName(u"Placement_page_officer_page")
        self.frame_17 = QFrame(self.Placement_page_officer_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(10, 10, 1111, 401))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_17)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_44 = QLabel(self.frame_17)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color :White;")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_44)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_19)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_72 = QLabel(self.frame_19)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_23.addWidget(self.label_72)

        self.label_45 = QLabel(self.frame_19)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_23.addWidget(self.label_45)

        self.label_73 = QLabel(self.frame_19)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_23.addWidget(self.label_73)

        self.label_74 = QLabel(self.frame_19)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_23.addWidget(self.label_74)

        self.label_75 = QLabel(self.frame_19)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_23.addWidget(self.label_75)


        self.horizontalLayout_5.addWidget(self.frame_19)

        self.frame_24 = QFrame(self.frame_18)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_24)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.textEdit_9 = QTextEdit(self.frame_24)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_28.addWidget(self.textEdit_9)

        self.textEdit_11 = QTextEdit(self.frame_24)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_28.addWidget(self.textEdit_11)

        self.comboBox_3 = QComboBox(self.frame_24)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_28.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.frame_24)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_28.addWidget(self.comboBox_4)

        self.textEdit_12 = QTextEdit(self.frame_24)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_28.addWidget(self.textEdit_12)


        self.horizontalLayout_5.addWidget(self.frame_24)


        self.verticalLayout_27.addWidget(self.frame_18)

        self.frame_25 = QFrame(self.frame_17)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_146 = QLabel(self.frame_25)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font1)
        self.label_146.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.horizontalLayout_6.addWidget(self.label_146)

        self.textEdit_29 = QTextEdit(self.frame_25)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.textEdit_29)

        self.pushButton_10 = QPushButton(self.frame_25)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_27.addWidget(self.frame_25)

        self.pushButton_4 = QPushButton(self.frame_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color:white;")

        self.verticalLayout_27.addWidget(self.pushButton_4)

        self.stackedWidget.addWidget(self.Placement_page_officer_page)
        self.placement_Officer_page = QWidget()
        self.placement_Officer_page.setObjectName(u"placement_Officer_page")
        self.frame_3 = QFrame(self.placement_Officer_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 20, 1051, 311))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_67 = QLabel(self.frame_3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font)
        self.label_67.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.verticalLayout_4.addWidget(self.label_67)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_9 = QLineEdit(self.frame_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_3.addWidget(self.lineEdit_9, 1, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_3.addWidget(self.lineEdit_10, 1, 2, 1, 1)

        self.label_58 = QLabel(self.frame_7)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)
        self.label_58.setStyleSheet(u"color:black")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_58, 0, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_3.addWidget(self.lineEdit_11, 1, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_7)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit_12, 1, 3, 1, 1)

        self.label_59 = QLabel(self.frame_7)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)
        self.label_59.setStyleSheet(u"color:black")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_59, 0, 0, 1, 1)

        self.label_60 = QLabel(self.frame_7)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)
        self.label_60.setStyleSheet(u"")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_60, 0, 3, 1, 1)

        self.label_61 = QLabel(self.frame_7)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)
        self.label_61.setStyleSheet(u"color:black")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_61, 0, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_14 = QLineEdit(self.frame_10)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit_14, 3, 1, 1, 1)

        self.label_62 = QLabel(self.frame_10)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font1)
        self.label_62.setStyleSheet(u"color:black")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_62, 0, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.frame_10)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_4.addWidget(self.lineEdit_15, 3, 3, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_10)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_4.addWidget(self.lineEdit_16, 3, 4, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame_10)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit_17, 3, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.frame_10)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_4.addWidget(self.lineEdit_18, 3, 2, 1, 1)

        self.label_63 = QLabel(self.frame_10)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font1)
        self.label_63.setStyleSheet(u"color:black")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_63, 0, 4, 1, 1)

        self.label_64 = QLabel(self.frame_10)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font1)
        self.label_64.setStyleSheet(u"color:black")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_64, 0, 3, 1, 1)

        self.label_65 = QLabel(self.frame_10)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font1)
        self.label_65.setStyleSheet(u"color:black")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_65, 0, 1, 1, 1)

        self.label_66 = QLabel(self.frame_10)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font1)
        self.label_66.setStyleSheet(u"color:black")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_66, 0, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.label_57 = QLabel(self.frame_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"background-color: rgb(24, 45	, 52);\n"
"\n"
"color:white;")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_57)

        self.stackedWidget.addWidget(self.placement_Officer_page)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.frame_26 = QFrame(self.page_5)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(10, 10, 1111, 401))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_26)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_46 = QLabel(self.frame_26)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color :White;")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_46)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_28)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_68 = QLabel(self.frame_28)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_30.addWidget(self.label_68)

        self.label_47 = QLabel(self.frame_28)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_30.addWidget(self.label_47)

        self.label_69 = QLabel(self.frame_28)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_30.addWidget(self.label_69)

        self.label_70 = QLabel(self.frame_28)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_30.addWidget(self.label_70)

        self.label_71 = QLabel(self.frame_28)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.verticalLayout_30.addWidget(self.label_71)


        self.horizontalLayout_7.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_29)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.textEdit_13 = QTextEdit(self.frame_29)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_31.addWidget(self.textEdit_13)

        self.textEdit_14 = QTextEdit(self.frame_29)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_31.addWidget(self.textEdit_14)

        self.comboBox_5 = QComboBox(self.frame_29)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_31.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.frame_29)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout_31.addWidget(self.comboBox_6)

        self.textEdit_15 = QTextEdit(self.frame_29)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_31.addWidget(self.textEdit_15)


        self.horizontalLayout_7.addWidget(self.frame_29)


        self.verticalLayout_29.addWidget(self.frame_27)

        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_147 = QLabel(self.frame_30)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font1)
        self.label_147.setStyleSheet(u"QLabel{font-size:22;}\n"
"")

        self.horizontalLayout_8.addWidget(self.label_147)

        self.textEdit_30 = QTextEdit(self.frame_30)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_8.addWidget(self.textEdit_30)

        self.pushButton_12 = QPushButton(self.frame_30)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_8.addWidget(self.pushButton_12)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_29.addWidget(self.frame_30)

        self.pushButton_3 = QPushButton(self.frame_26)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color:white;")

        self.verticalLayout_29.addWidget(self.pushButton_3)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 50, 401, 51))
        font3 = QFont()
        font3.setPointSize(27)
        self.label_9.setFont(font3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_10 = QLabel(self.page_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 60, 401, 51))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_11 = QLabel(self.page_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 50, 401, 51))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_12 = QLabel(self.page_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 60, 401, 51))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_9)
        self.Inactive_personnel_page_01 = QWidget()
        self.Inactive_personnel_page_01.setObjectName(u"Inactive_personnel_page_01")
        self.verticalLayout_10 = QVBoxLayout(self.Inactive_personnel_page_01)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_33 = QLabel(self.Inactive_personnel_page_01)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setLayoutDirection(Qt.LeftToRight)
        self.label_33.setStyleSheet(u"color:white;\n"
"background-color: rgb(98, 160, 234);")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_33)

        self.frame_8 = QFrame(self.Inactive_personnel_page_01)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_19 = QLineEdit(self.frame_8)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_5.addWidget(self.lineEdit_19, 1, 1, 1, 1)

        self.lineEdit_20 = QLineEdit(self.frame_8)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_5.addWidget(self.lineEdit_20, 1, 2, 1, 1)

        self.label_34 = QLabel(self.frame_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"color:black")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_34, 0, 2, 1, 1)

        self.lineEdit_21 = QLineEdit(self.frame_8)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_5.addWidget(self.lineEdit_21, 1, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.frame_8)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_22, 1, 3, 1, 1)

        self.label_35 = QLabel(self.frame_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"color:black")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_36 = QLabel(self.frame_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)
        self.label_36.setStyleSheet(u"")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_36, 0, 3, 1, 1)

        self.label_37 = QLabel(self.frame_8)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)
        self.label_37.setStyleSheet(u"color:black")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_37, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.Inactive_personnel_page_01)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_23 = QLineEdit(self.frame_9)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.lineEdit_23, 3, 1, 1, 1)

        self.label_38 = QLabel(self.frame_9)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"color:black")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_38, 0, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.frame_9)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_6.addWidget(self.lineEdit_24, 3, 3, 1, 1)

        self.lineEdit_25 = QLineEdit(self.frame_9)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_6.addWidget(self.lineEdit_25, 3, 4, 1, 1)

        self.lineEdit_26 = QLineEdit(self.frame_9)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.lineEdit_26, 3, 0, 1, 1)

        self.lineEdit_27 = QLineEdit(self.frame_9)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_6.addWidget(self.lineEdit_27, 3, 2, 1, 1)

        self.label_39 = QLabel(self.frame_9)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)
        self.label_39.setStyleSheet(u"color:black")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_39, 0, 4, 1, 1)

        self.label_40 = QLabel(self.frame_9)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)
        self.label_40.setStyleSheet(u"color:black")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_40, 0, 3, 1, 1)

        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font1)
        self.label_41.setStyleSheet(u"color:black")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_41, 0, 1, 1, 1)

        self.label_42 = QLabel(self.frame_9)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)
        self.label_42.setStyleSheet(u"color:black")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_42, 0, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.label_43 = QLabel(self.Inactive_personnel_page_01)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"\n"
"color:white;")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_43)

        self.tableWidget = QTableWidget(self.Inactive_personnel_page_01)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(167)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_10.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.Inactive_personnel_page_01)

        self.verticalLayout_24.addWidget(self.stackedWidget)


        self.verticalLayout_21.addWidget(self.main_widget)


        self.gridLayout_13.addWidget(self.frame_23, 1, 1, 1, 1)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_22)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_text_widget = QWidget(self.frame_22)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.icon_text_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 500))
        self.scrollArea.setStyleSheet(u"QScrollBar::handle:vertical{\n"
"border:none;\n"
"border-radius:7px;\n"
"width:14px;\n"
"margin: 15px 0 15px 0;\n"
"background-color: rgb(98, 160, 234);\n"
"\n"
"\n"
"}")
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 282, 1501))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.personnel_recordsbtn = QPushButton(self.scrollAreaWidgetContents)
        self.personnel_recordsbtn.setObjectName(u"personnel_recordsbtn")
        font4 = QFont()
        font4.setFamilies([u"Ubuntu Mono"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.personnel_recordsbtn.setFont(font4)
        self.personnel_recordsbtn.setStyleSheet(u"")
        self.personnel_recordsbtn.setIconSize(QSize(30, 30))
        self.personnel_recordsbtn.setCheckable(False)
        self.personnel_recordsbtn.setFlat(True)

        self.verticalLayout.addWidget(self.personnel_recordsbtn)

        self.placement_btn = QPushButton(self.scrollAreaWidgetContents)
        self.placement_btn.setObjectName(u"placement_btn")
        self.placement_btn.setFont(font4)
        self.placement_btn.setStyleSheet(u"")
        self.placement_btn.setIconSize(QSize(30, 30))
        self.placement_btn.setCheckable(True)
        self.placement_btn.setFlat(True)

        self.verticalLayout.addWidget(self.placement_btn)

        self.placement_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.placement_dropdown.setObjectName(u"placement_dropdown")
        self.placement_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.placement_dropdown.setFrameShape(QFrame.StyledPanel)
        self.placement_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.placement_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.palcement_offr_btn = QPushButton(self.placement_dropdown)
        self.palcement_offr_btn.setObjectName(u"palcement_offr_btn")
        self.palcement_offr_btn.setCheckable(False)
        self.palcement_offr_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.palcement_offr_btn)

        self.placementenlist_btn = QPushButton(self.placement_dropdown)
        self.placementenlist_btn.setObjectName(u"placementenlist_btn")
        self.placementenlist_btn.setCheckable(False)
        self.placementenlist_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.placementenlist_btn)

        self.pushButton_27 = QPushButton(self.placement_dropdown)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setCheckable(False)
        self.pushButton_27.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.placement_dropdown)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setCheckable(False)
        self.pushButton_28.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_28)


        self.verticalLayout.addWidget(self.placement_dropdown)

        self.reenlistment_btn = QPushButton(self.scrollAreaWidgetContents)
        self.reenlistment_btn.setObjectName(u"reenlistment_btn")
        self.reenlistment_btn.setFont(font4)
        self.reenlistment_btn.setStyleSheet(u"")
        self.reenlistment_btn.setIconSize(QSize(30, 30))
        self.reenlistment_btn.setCheckable(True)
        self.reenlistment_btn.setFlat(True)

        self.verticalLayout.addWidget(self.reenlistment_btn)

        self.reenlistmen_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.reenlistmen_dropdown.setObjectName(u"reenlistmen_dropdown")
        self.reenlistmen_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.reenlistmen_dropdown.setFrameShape(QFrame.StyledPanel)
        self.reenlistmen_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.reenlistmen_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_30 = QPushButton(self.reenlistmen_dropdown)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setCheckable(False)
        self.pushButton_30.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_30)

        self.pushButton_31 = QPushButton(self.reenlistmen_dropdown)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setCheckable(False)
        self.pushButton_31.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.reenlistmen_dropdown)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setCheckable(False)
        self.pushButton_32.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_32)

        self.pushButton_33 = QPushButton(self.reenlistmen_dropdown)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setCheckable(False)
        self.pushButton_33.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_33)


        self.verticalLayout.addWidget(self.reenlistmen_dropdown)

        self.schooling_btn = QPushButton(self.scrollAreaWidgetContents)
        self.schooling_btn.setObjectName(u"schooling_btn")
        self.schooling_btn.setFont(font4)
        self.schooling_btn.setStyleSheet(u"")
        self.schooling_btn.setIconSize(QSize(30, 30))
        self.schooling_btn.setCheckable(True)
        self.schooling_btn.setFlat(True)

        self.verticalLayout.addWidget(self.schooling_btn)

        self.seniority_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.seniority_dropdown.setObjectName(u"seniority_dropdown")
        self.seniority_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.seniority_dropdown.setFrameShape(QFrame.StyledPanel)
        self.seniority_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.seniority_dropdown)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton_46 = QPushButton(self.seniority_dropdown)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setCheckable(True)
        self.pushButton_46.setFlat(True)

        self.verticalLayout_15.addWidget(self.pushButton_46)

        self.officerschooling_dropdown = QFrame(self.seniority_dropdown)
        self.officerschooling_dropdown.setObjectName(u"officerschooling_dropdown")
        self.officerschooling_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.officerschooling_dropdown.setFrameShape(QFrame.StyledPanel)
        self.officerschooling_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.officerschooling_dropdown)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_48 = QPushButton(self.officerschooling_dropdown)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setCheckable(False)
        self.pushButton_48.setFlat(True)

        self.verticalLayout_17.addWidget(self.pushButton_48)

        self.pushButton_49 = QPushButton(self.officerschooling_dropdown)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setCheckable(False)
        self.pushButton_49.setFlat(True)

        self.verticalLayout_17.addWidget(self.pushButton_49)

        self.pushButton_50 = QPushButton(self.officerschooling_dropdown)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setCheckable(False)
        self.pushButton_50.setFlat(True)

        self.verticalLayout_17.addWidget(self.pushButton_50)


        self.verticalLayout_15.addWidget(self.officerschooling_dropdown)

        self.pushButton_47 = QPushButton(self.seniority_dropdown)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setCheckable(True)
        self.pushButton_47.setFlat(True)

        self.verticalLayout_15.addWidget(self.pushButton_47)

        self.elinstschooling_dropdown = QFrame(self.seniority_dropdown)
        self.elinstschooling_dropdown.setObjectName(u"elinstschooling_dropdown")
        self.elinstschooling_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;color:white\n"
"\n"
"}\n"
"")
        self.elinstschooling_dropdown.setFrameShape(QFrame.StyledPanel)
        self.elinstschooling_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.elinstschooling_dropdown)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_52 = QPushButton(self.elinstschooling_dropdown)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setCheckable(False)
        self.pushButton_52.setFlat(True)

        self.verticalLayout_19.addWidget(self.pushButton_52)

        self.pushButton_53 = QPushButton(self.elinstschooling_dropdown)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setCheckable(False)
        self.pushButton_53.setFlat(True)

        self.verticalLayout_19.addWidget(self.pushButton_53)

        self.pushButton_51 = QPushButton(self.elinstschooling_dropdown)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setCheckable(False)
        self.pushButton_51.setFlat(True)

        self.verticalLayout_19.addWidget(self.pushButton_51)

        self.pushButton_54 = QPushButton(self.elinstschooling_dropdown)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setCheckable(False)
        self.pushButton_54.setFlat(True)

        self.verticalLayout_19.addWidget(self.pushButton_54)


        self.verticalLayout_15.addWidget(self.elinstschooling_dropdown)


        self.verticalLayout.addWidget(self.seniority_dropdown)

        self.promotion_btn = QPushButton(self.scrollAreaWidgetContents)
        self.promotion_btn.setObjectName(u"promotion_btn")
        self.promotion_btn.setFont(font4)
        self.promotion_btn.setStyleSheet(u"")
        self.promotion_btn.setIconSize(QSize(30, 30))
        self.promotion_btn.setCheckable(True)
        self.promotion_btn.setFlat(True)

        self.verticalLayout.addWidget(self.promotion_btn)

        self.promotion_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.promotion_dropdown.setObjectName(u"promotion_dropdown")
        self.promotion_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.promotion_dropdown.setFrameShape(QFrame.StyledPanel)
        self.promotion_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.promotion_dropdown)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_40 = QPushButton(self.promotion_dropdown)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setCheckable(False)
        self.pushButton_40.setFlat(True)

        self.verticalLayout_9.addWidget(self.pushButton_40)

        self.pushButton_41 = QPushButton(self.promotion_dropdown)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setCheckable(False)
        self.pushButton_41.setFlat(True)

        self.verticalLayout_9.addWidget(self.pushButton_41)


        self.verticalLayout.addWidget(self.promotion_dropdown)

        self.seniority_liner_btn = QPushButton(self.scrollAreaWidgetContents)
        self.seniority_liner_btn.setObjectName(u"seniority_liner_btn")
        self.seniority_liner_btn.setFont(font4)
        self.seniority_liner_btn.setStyleSheet(u"")
        self.seniority_liner_btn.setIconSize(QSize(30, 30))
        self.seniority_liner_btn.setCheckable(True)
        self.seniority_liner_btn.setFlat(True)

        self.verticalLayout.addWidget(self.seniority_liner_btn)

        self.schooling_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.schooling_dropdown.setObjectName(u"schooling_dropdown")
        self.schooling_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.schooling_dropdown.setFrameShape(QFrame.StyledPanel)
        self.schooling_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.schooling_dropdown)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_36 = QPushButton(self.schooling_dropdown)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setFlat(True)

        self.verticalLayout_5.addWidget(self.pushButton_36)

        self.pushButton_37 = QPushButton(self.schooling_dropdown)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setFlat(True)

        self.verticalLayout_5.addWidget(self.pushButton_37)


        self.verticalLayout.addWidget(self.schooling_dropdown)

        self.afscmonitoring_btn = QPushButton(self.scrollAreaWidgetContents)
        self.afscmonitoring_btn.setObjectName(u"afscmonitoring_btn")
        self.afscmonitoring_btn.setFont(font4)
        self.afscmonitoring_btn.setStyleSheet(u"")
        self.afscmonitoring_btn.setIconSize(QSize(30, 30))
        self.afscmonitoring_btn.setCheckable(True)
        self.afscmonitoring_btn.setFlat(True)

        self.verticalLayout.addWidget(self.afscmonitoring_btn)

        self.afsc_monitoring_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.afsc_monitoring_dropdown.setObjectName(u"afsc_monitoring_dropdown")
        self.afsc_monitoring_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.afsc_monitoring_dropdown.setFrameShape(QFrame.StyledPanel)
        self.afsc_monitoring_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.afsc_monitoring_dropdown)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_42 = QPushButton(self.afsc_monitoring_dropdown)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setCheckable(False)
        self.pushButton_42.setFlat(True)

        self.verticalLayout_11.addWidget(self.pushButton_42)

        self.pushButton_43 = QPushButton(self.afsc_monitoring_dropdown)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setCheckable(False)
        self.pushButton_43.setFlat(True)

        self.verticalLayout_11.addWidget(self.pushButton_43)


        self.verticalLayout.addWidget(self.afsc_monitoring_dropdown)

        self.etad_sot_btn = QPushButton(self.scrollAreaWidgetContents)
        self.etad_sot_btn.setObjectName(u"etad_sot_btn")
        self.etad_sot_btn.setFont(font4)
        self.etad_sot_btn.setStyleSheet(u"")
        self.etad_sot_btn.setIconSize(QSize(30, 30))
        self.etad_sot_btn.setCheckable(True)
        self.etad_sot_btn.setFlat(True)

        self.verticalLayout.addWidget(self.etad_sot_btn)

        self.etad_SOT_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.etad_SOT_dropdown.setObjectName(u"etad_SOT_dropdown")
        self.etad_SOT_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.etad_SOT_dropdown.setFrameShape(QFrame.StyledPanel)
        self.etad_SOT_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.etad_SOT_dropdown)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_34 = QPushButton(self.etad_SOT_dropdown)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setCheckable(False)
        self.pushButton_34.setFlat(True)

        self.verticalLayout_13.addWidget(self.pushButton_34)

        self.pushButton_35 = QPushButton(self.etad_SOT_dropdown)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setCheckable(False)
        self.pushButton_35.setFlat(True)

        self.verticalLayout_13.addWidget(self.pushButton_35)

        self.pushButton_44 = QPushButton(self.etad_SOT_dropdown)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setCheckable(False)
        self.pushButton_44.setFlat(True)

        self.verticalLayout_13.addWidget(self.pushButton_44)

        self.pushButton_45 = QPushButton(self.etad_SOT_dropdown)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setCheckable(False)
        self.pushButton_45.setFlat(True)

        self.verticalLayout_13.addWidget(self.pushButton_45)


        self.verticalLayout.addWidget(self.etad_SOT_dropdown)

        self.attrition_btn = QPushButton(self.scrollAreaWidgetContents)
        self.attrition_btn.setObjectName(u"attrition_btn")
        self.attrition_btn.setFont(font4)
        self.attrition_btn.setStyleSheet(u"")
        self.attrition_btn.setIconSize(QSize(30, 30))
        self.attrition_btn.setCheckable(True)
        self.attrition_btn.setFlat(True)

        self.verticalLayout.addWidget(self.attrition_btn)

        self.attrition_dropdown = QFrame(self.scrollAreaWidgetContents)
        self.attrition_dropdown.setObjectName(u"attrition_dropdown")
        self.attrition_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"\n"
"background-color: #1a659e;\n"
"color:white\n"
"\n"
"}\n"
"")
        self.attrition_dropdown.setFrameShape(QFrame.StyledPanel)
        self.attrition_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.attrition_dropdown)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_55 = QPushButton(self.attrition_dropdown)
        self.pushButton_55.setObjectName(u"pushButton_55")
        self.pushButton_55.setCheckable(False)
        self.pushButton_55.setFlat(True)

        self.verticalLayout_16.addWidget(self.pushButton_55)

        self.pushButton_56 = QPushButton(self.attrition_dropdown)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setCheckable(False)
        self.pushButton_56.setFlat(True)

        self.verticalLayout_16.addWidget(self.pushButton_56)


        self.verticalLayout.addWidget(self.attrition_dropdown)

        self.inactivepersonnel_btn = QPushButton(self.scrollAreaWidgetContents)
        self.inactivepersonnel_btn.setObjectName(u"inactivepersonnel_btn")
        self.inactivepersonnel_btn.setFont(font4)
        self.inactivepersonnel_btn.setStyleSheet(u"")
        self.inactivepersonnel_btn.setIconSize(QSize(30, 30))
        self.inactivepersonnel_btn.setCheckable(False)
        self.inactivepersonnel_btn.setFlat(True)

        self.verticalLayout.addWidget(self.inactivepersonnel_btn)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 204, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.icon_text_widget)


        self.gridLayout_13.addWidget(self.frame_22, 1, 0, 1, 1)

        self.gridLayout_13.setRowStretch(0, 1)
        self.gridLayout_13.setRowStretch(1, 8)
        self.gridLayout_13.setColumnStretch(0, 2)
        self.gridLayout_13.setColumnStretch(1, 8)

        self.verticalLayout_20.addWidget(self.frame_20)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.afscmonitoring_btn.toggled.connect(self.afsc_monitoring_dropdown.setVisible)
        self.placement_btn.toggled.connect(self.placement_dropdown.setVisible)
        self.seniority_liner_btn.toggled.connect(self.schooling_dropdown.setVisible)
        self.pushButton_46.toggled.connect(self.officerschooling_dropdown.setVisible)
        self.attrition_btn.toggled.connect(self.attrition_dropdown.setVisible)
        self.pushButton_47.toggled.connect(self.elinstschooling_dropdown.setVisible)
        self.schooling_btn.toggled.connect(self.seniority_dropdown.setVisible)
        self.etad_sot_btn.toggled.connect(self.etad_SOT_dropdown.setVisible)
        self.reenlistment_btn.toggled.connect(self.reenlistmen_dropdown.setVisible)
        self.promotion_btn.toggled.connect(self.promotion_dropdown.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAF HUMAN RESOURCES MANAGEMENT SYSTEM", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ACTIVE PERSONNEL RECORDS", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sufffix", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"AFPSN", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Rank", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NR", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"AFSN", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"RANK", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"UNIT", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"FULLNAME", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ACTION", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"PERSONAL DETAILS", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Present Unit:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Reassignment unit", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Sub unit", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Reassignment Date", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Upload Order:", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"PERSONAL DETAILS", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Present Unit:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Reassignment unit", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Sub unit", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Reassignment Date", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Upload Order:", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"ACTIVE PERSONNEL RECORDS", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Sufffix", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"AFPSN", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Unit", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Rank", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"PERSONAL DETAILS", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Present Unit:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Reassignment unit", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Sub unit", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Reassignment Date", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Upload Order:", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SENIORITY LINEAR LIST", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"AFSC MONITORING", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ETAD / SOT", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ATTRITION", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"INACTIVE PERSONNEL ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Sufffix", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"AFPSN", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Source of Enlistment", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Rank", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Classification", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"NR", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"AFSN", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"RANK", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"FULLNAME", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"UNIT", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ACTION", None));
        self.personnel_recordsbtn.setText(QCoreApplication.translate("MainWindow", u"PERSONNEL RECORDS", None))
        self.placement_btn.setText(QCoreApplication.translate("MainWindow", u"PLACEMENT", None))
        self.palcement_offr_btn.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.placementenlist_btn.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"DS MONITORING", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PERSONNEL MONITORING", None))
        self.reenlistment_btn.setText(QCoreApplication.translate("MainWindow", u"REENLISTMENT", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"1ST TRANCHE", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"2ND TRANCHE/RE-ENLISTMENT", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"FOR MEDICAL", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"EXPIRED ETE", None))
        self.schooling_btn.setText(QCoreApplication.translate("MainWindow", u"SCHOOLING", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"CGSC", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"BAFOC", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"ANCOC", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"BNCOC", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"SMC", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"BMT", None))
        self.promotion_btn.setText(QCoreApplication.translate("MainWindow", u"PROMOTION", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.seniority_liner_btn.setText(QCoreApplication.translate("MainWindow", u"SENIORITY LINEAR LIST", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.afscmonitoring_btn.setText(QCoreApplication.translate("MainWindow", u"AFSC MONITORING", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PRIORITY COURSES", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"BY UNIT", None))
        self.etad_sot_btn.setText(QCoreApplication.translate("MainWindow", u"ETAD / SOT", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"SOT", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"2ND ETAD", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"1ST ETAD", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PROVISIONAL", None))
        self.attrition_btn.setText(QCoreApplication.translate("MainWindow", u"ATTRITION", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.inactivepersonnel_btn.setText(QCoreApplication.translate("MainWindow", u"INACTIVE PERSONNEL", None))
    # retranslateUi

