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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1368, 814)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setGeometry(QRect(0, 80, 371, 861))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
"color:white\n"
"\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.personnel_recordsbtn = QPushButton(self.icon_text_widget)
        self.personnel_recordsbtn.setObjectName(u"personnel_recordsbtn")
        font = QFont()
        font.setFamilies([u"Ubuntu Mono"])
        font.setPointSize(18)
        font.setBold(True)
        self.personnel_recordsbtn.setFont(font)
        self.personnel_recordsbtn.setStyleSheet(u"")
        self.personnel_recordsbtn.setIconSize(QSize(30, 30))
        self.personnel_recordsbtn.setCheckable(False)

        self.verticalLayout.addWidget(self.personnel_recordsbtn)

        self.placement_btn = QPushButton(self.icon_text_widget)
        self.placement_btn.setObjectName(u"placement_btn")
        self.placement_btn.setFont(font)
        self.placement_btn.setStyleSheet(u"")
        self.placement_btn.setIconSize(QSize(30, 30))
        self.placement_btn.setCheckable(True)
        self.placement_btn.setFlat(False)

        self.verticalLayout.addWidget(self.placement_btn)

        self.reenlistment_btn = QPushButton(self.icon_text_widget)
        self.reenlistment_btn.setObjectName(u"reenlistment_btn")
        self.reenlistment_btn.setFont(font)
        self.reenlistment_btn.setStyleSheet(u"")
        self.reenlistment_btn.setIconSize(QSize(30, 30))
        self.reenlistment_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.reenlistment_btn)

        self.schooling_btn = QPushButton(self.icon_text_widget)
        self.schooling_btn.setObjectName(u"schooling_btn")
        self.schooling_btn.setFont(font)
        self.schooling_btn.setStyleSheet(u"")
        self.schooling_btn.setIconSize(QSize(30, 30))
        self.schooling_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.schooling_btn)

        self.promotion_btn = QPushButton(self.icon_text_widget)
        self.promotion_btn.setObjectName(u"promotion_btn")
        self.promotion_btn.setFont(font)
        self.promotion_btn.setStyleSheet(u"")
        self.promotion_btn.setIconSize(QSize(30, 30))
        self.promotion_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.promotion_btn)

        self.seniority_liner_btn = QPushButton(self.icon_text_widget)
        self.seniority_liner_btn.setObjectName(u"seniority_liner_btn")
        self.seniority_liner_btn.setFont(font)
        self.seniority_liner_btn.setStyleSheet(u"")
        self.seniority_liner_btn.setIconSize(QSize(30, 30))
        self.seniority_liner_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.seniority_liner_btn)

        self.afscmonitoring_btn = QPushButton(self.icon_text_widget)
        self.afscmonitoring_btn.setObjectName(u"afscmonitoring_btn")
        self.afscmonitoring_btn.setFont(font)
        self.afscmonitoring_btn.setStyleSheet(u"")
        self.afscmonitoring_btn.setIconSize(QSize(30, 30))
        self.afscmonitoring_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.afscmonitoring_btn)

        self.etad_sot_btn = QPushButton(self.icon_text_widget)
        self.etad_sot_btn.setObjectName(u"etad_sot_btn")
        self.etad_sot_btn.setFont(font)
        self.etad_sot_btn.setStyleSheet(u"")
        self.etad_sot_btn.setIconSize(QSize(30, 30))
        self.etad_sot_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.etad_sot_btn)

        self.attrition_btn = QPushButton(self.icon_text_widget)
        self.attrition_btn.setObjectName(u"attrition_btn")
        self.attrition_btn.setFont(font)
        self.attrition_btn.setStyleSheet(u"")
        self.attrition_btn.setIconSize(QSize(30, 30))
        self.attrition_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.attrition_btn)

        self.inactivepersonnel_btn = QPushButton(self.icon_text_widget)
        self.inactivepersonnel_btn.setObjectName(u"inactivepersonnel_btn")
        self.inactivepersonnel_btn.setFont(font)
        self.inactivepersonnel_btn.setStyleSheet(u"")
        self.inactivepersonnel_btn.setIconSize(QSize(30, 30))
        self.inactivepersonnel_btn.setCheckable(False)

        self.verticalLayout.addWidget(self.inactivepersonnel_btn)

        self.verticalSpacer = QSpacerItem(20, 450, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setGeometry(QRect(370, 80, 941, 971))
        self.main_widget.setStyleSheet(u"background-color:#f8f9fa;\n"
"")
        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 911, 731))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 921, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(98, 160, 234);")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 50, 911, 201))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color:black")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color:black")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 0, 3, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color:black")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color:black")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.frame_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_2.addWidget(self.lineEdit_13, 3, 3, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_2.addWidget(self.lineEdit_8, 3, 4, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_2.addWidget(self.lineEdit_7, 3, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 3, 2, 1, 1)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"color:black")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_21, 0, 4, 1, 1)

        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"color:black")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_26, 0, 3, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color:black")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_18, 0, 1, 1, 1)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color:black")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_19, 0, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.label_27 = QLabel(self.page)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 270, 921, 41))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"background-color: rgb(24, 45	, 52);\n"
"\n"
"color:white;")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.PersonnelRecords_table = QTableWidget(self.page)
        if (self.PersonnelRecords_table.columnCount() < 5):
            self.PersonnelRecords_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.PersonnelRecords_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.PersonnelRecords_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.PersonnelRecords_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.PersonnelRecords_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.PersonnelRecords_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.PersonnelRecords_table.setObjectName(u"PersonnelRecords_table")
        self.PersonnelRecords_table.setGeometry(QRect(0, 320, 911, 401))
        self.PersonnelRecords_table.setStyleSheet(u"color:black")
        self.PersonnelRecords_table.setShowGrid(False)
        self.PersonnelRecords_table.setGridStyle(Qt.SolidLine)
        self.PersonnelRecords_table.horizontalHeader().setVisible(True)
        self.PersonnelRecords_table.horizontalHeader().setCascadingSectionResizes(False)
        self.PersonnelRecords_table.horizontalHeader().setDefaultSectionSize(181)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 50, 371, 51))
        font3 = QFont()
        font3.setPointSize(27)
        self.label_5.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 20, 401, 51))
        self.label_6.setFont(font3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 50, 401, 51))
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 40, 401, 51))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 50, 401, 51))
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
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_13 = QLabel(self.page_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 60, 401, 51))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.page_10)
        self.top_widget = QWidget(self.centralwidget)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setGeometry(QRect(0, 0, 1331, 81))
        self.top_widget.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(0, 62, 63);\n"
"color:white;\n"
"}")
        self.label = QLabel(self.top_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/newPrefix/icon/Logo.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.top_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 10, 451, 51))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font-size:20px;\n"
"\n"
"}")
        self.pushButton_24 = QPushButton(self.top_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(1190, 20, 101, 41))
        icon = QIcon()
        icon.addFile(u":/ /icon/PersonalRecords.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon)
        self.pushButton_24.setIconSize(QSize(40, 40))
        self.pushButton_11 = QPushButton(self.top_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(1040, 20, 121, 41))
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QSize(40, 40))
        self.placement_dropdown = QFrame(self.centralwidget)
        self.placement_dropdown.setObjectName(u"placement_dropdown")
        self.placement_dropdown.setGeometry(QRect(370, 80, 241, 151))
        self.placement_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
"color:white\n"
"\n"
"}\n"
"")
        self.placement_dropdown.setFrameShape(QFrame.StyledPanel)
        self.placement_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.placement_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_25 = QPushButton(self.placement_dropdown)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_25)

        self.pushButton_27 = QPushButton(self.placement_dropdown)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_27)

        self.pushButton_26 = QPushButton(self.placement_dropdown)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_26)

        self.pushButton_28 = QPushButton(self.placement_dropdown)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_28)

        self.reenlistmen_dropdown = QFrame(self.centralwidget)
        self.reenlistmen_dropdown.setObjectName(u"reenlistmen_dropdown")
        self.reenlistmen_dropdown.setGeometry(QRect(370, 120, 321, 141))
        self.reenlistmen_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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

        self.verticalLayout_3.addWidget(self.pushButton_30)

        self.pushButton_31 = QPushButton(self.reenlistmen_dropdown)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.reenlistmen_dropdown)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton_32)

        self.pushButton_33 = QPushButton(self.reenlistmen_dropdown)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton_33)

        self.schooling_dropdown = QFrame(self.centralwidget)
        self.schooling_dropdown.setObjectName(u"schooling_dropdown")
        self.schooling_dropdown.setGeometry(QRect(370, 170, 281, 101))
        self.schooling_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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
        self.pushButton_36.setCheckable(True)

        self.verticalLayout_5.addWidget(self.pushButton_36)

        self.pushButton_37 = QPushButton(self.schooling_dropdown)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setCheckable(True)

        self.verticalLayout_5.addWidget(self.pushButton_37)

        self.elinstschooling_dropdown = QFrame(self.centralwidget)
        self.elinstschooling_dropdown.setObjectName(u"elinstschooling_dropdown")
        self.elinstschooling_dropdown.setGeometry(QRect(640, 150, 281, 151))
        self.elinstschooling_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
"color:white\n"
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

        self.verticalLayout_19.addWidget(self.pushButton_52)

        self.pushButton_53 = QPushButton(self.elinstschooling_dropdown)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setCheckable(False)

        self.verticalLayout_19.addWidget(self.pushButton_53)

        self.pushButton_51 = QPushButton(self.elinstschooling_dropdown)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setCheckable(False)

        self.verticalLayout_19.addWidget(self.pushButton_51)

        self.pushButton_54 = QPushButton(self.elinstschooling_dropdown)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setCheckable(False)

        self.verticalLayout_19.addWidget(self.pushButton_54)

        self.officerschooling_dropdown = QFrame(self.centralwidget)
        self.officerschooling_dropdown.setObjectName(u"officerschooling_dropdown")
        self.officerschooling_dropdown.setGeometry(QRect(640, 150, 281, 151))
        self.officerschooling_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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

        self.verticalLayout_17.addWidget(self.pushButton_48)

        self.pushButton_49 = QPushButton(self.officerschooling_dropdown)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setCheckable(False)

        self.verticalLayout_17.addWidget(self.pushButton_49)

        self.pushButton_50 = QPushButton(self.officerschooling_dropdown)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setCheckable(False)

        self.verticalLayout_17.addWidget(self.pushButton_50)

        self.afsc_monitoring_dropdown = QFrame(self.centralwidget)
        self.afsc_monitoring_dropdown.setObjectName(u"afsc_monitoring_dropdown")
        self.afsc_monitoring_dropdown.setGeometry(QRect(370, 290, 281, 101))
        self.afsc_monitoring_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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

        self.verticalLayout_11.addWidget(self.pushButton_42)

        self.pushButton_43 = QPushButton(self.afsc_monitoring_dropdown)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setCheckable(False)

        self.verticalLayout_11.addWidget(self.pushButton_43)

        self.promotion_dropdown = QFrame(self.centralwidget)
        self.promotion_dropdown.setObjectName(u"promotion_dropdown")
        self.promotion_dropdown.setGeometry(QRect(370, 210, 281, 101))
        self.promotion_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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

        self.verticalLayout_9.addWidget(self.pushButton_40)

        self.pushButton_41 = QPushButton(self.promotion_dropdown)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setCheckable(False)

        self.verticalLayout_9.addWidget(self.pushButton_41)

        self.etad_SOT_dropdown = QFrame(self.centralwidget)
        self.etad_SOT_dropdown.setObjectName(u"etad_SOT_dropdown")
        self.etad_SOT_dropdown.setGeometry(QRect(370, 250, 281, 191))
        self.etad_SOT_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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

        self.verticalLayout_13.addWidget(self.pushButton_34)

        self.pushButton_35 = QPushButton(self.etad_SOT_dropdown)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setCheckable(False)

        self.verticalLayout_13.addWidget(self.pushButton_35)

        self.pushButton_44 = QPushButton(self.etad_SOT_dropdown)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setCheckable(False)

        self.verticalLayout_13.addWidget(self.pushButton_44)

        self.pushButton_45 = QPushButton(self.etad_SOT_dropdown)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setCheckable(False)

        self.verticalLayout_13.addWidget(self.pushButton_45)

        self.seniority_dropdown = QFrame(self.centralwidget)
        self.seniority_dropdown.setObjectName(u"seniority_dropdown")
        self.seniority_dropdown.setGeometry(QRect(370, 250, 281, 111))
        self.seniority_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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
        self.pushButton_46.setCheckable(False)

        self.verticalLayout_15.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.seniority_dropdown)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setCheckable(False)

        self.verticalLayout_15.addWidget(self.pushButton_47)

        self.attrition_dropdown = QFrame(self.centralwidget)
        self.attrition_dropdown.setObjectName(u"attrition_dropdown")
        self.attrition_dropdown.setGeometry(QRect(370, 370, 281, 111))
        self.attrition_dropdown.setStyleSheet(u"QWidget{\n"
"\n"
"background-color: rgb(24, 45	, 52);\n"
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

        self.verticalLayout_16.addWidget(self.pushButton_55)

        self.pushButton_56 = QPushButton(self.attrition_dropdown)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setCheckable(False)

        self.verticalLayout_16.addWidget(self.pushButton_56)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_widget.raise_()
        self.icon_text_widget.raise_()
        self.top_widget.raise_()
        self.placement_dropdown.raise_()
        self.reenlistmen_dropdown.raise_()
        self.schooling_dropdown.raise_()
        self.elinstschooling_dropdown.raise_()
        self.officerschooling_dropdown.raise_()
        self.afsc_monitoring_dropdown.raise_()
        self.promotion_dropdown.raise_()
        self.etad_SOT_dropdown.raise_()
        self.seniority_dropdown.raise_()
        self.attrition_dropdown.raise_()

        self.retranslateUi(MainWindow)
        self.placement_btn.toggled.connect(self.placement_dropdown.setVisible)
        self.reenlistment_btn.toggled.connect(self.reenlistmen_dropdown.setVisible)
        self.pushButton_37.toggled.connect(self.elinstschooling_dropdown.setVisible)
        self.pushButton_36.toggled.connect(self.officerschooling_dropdown.setVisible)
        self.schooling_btn.toggled.connect(self.schooling_dropdown.setVisible)
        self.afscmonitoring_btn.toggled.connect(self.afsc_monitoring_dropdown.setVisible)
        self.promotion_btn.toggled.connect(self.promotion_dropdown.setVisible)
        self.seniority_liner_btn.toggled.connect(self.seniority_dropdown.setVisible)
        self.etad_sot_btn.toggled.connect(self.etad_SOT_dropdown.setVisible)
        self.attrition_btn.toggled.connect(self.attrition_dropdown.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.personnel_recordsbtn.setText(QCoreApplication.translate("MainWindow", u"PERSONNEL RECORDS", None))
        self.placement_btn.setText(QCoreApplication.translate("MainWindow", u"PLACEMENT", None))
        self.reenlistment_btn.setText(QCoreApplication.translate("MainWindow", u"REENLISTMENT", None))
        self.schooling_btn.setText(QCoreApplication.translate("MainWindow", u"SCHOOLING", None))
        self.promotion_btn.setText(QCoreApplication.translate("MainWindow", u"PROMOTION", None))
        self.seniority_liner_btn.setText(QCoreApplication.translate("MainWindow", u"SENIORITY LINEAR LIST", None))
        self.afscmonitoring_btn.setText(QCoreApplication.translate("MainWindow", u"AFSC MONITORING", None))
        self.etad_sot_btn.setText(QCoreApplication.translate("MainWindow", u"ETAD / SOT", None))
        self.attrition_btn.setText(QCoreApplication.translate("MainWindow", u"ATTRITION", None))
        self.inactivepersonnel_btn.setText(QCoreApplication.translate("MainWindow", u"INACTIVE PERSONNEL", None))
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
        ___qtablewidgetitem = self.PersonnelRecords_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NR", None));
        ___qtablewidgetitem1 = self.PersonnelRecords_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"AFPSN", None));
        ___qtablewidgetitem2 = self.PersonnelRecords_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"RANK", None));
        ___qtablewidgetitem3 = self.PersonnelRecords_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"FULL NAME", None));
        ___qtablewidgetitem4 = self.PersonnelRecords_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ACTION", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PLACEMENT", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"REENLISTMENT", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SCHOOLING", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PROMOTION", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SENIORITY LINEAR LIST", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"AFSC MONITORING", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ETAD / SOT", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ATTRITION", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"INACTIVE PERSONNEL", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAF HUMAN RESOURCES MANAGEMENT SYSTEM", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"DS MONITORING", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PERSONNEL MONITORING", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"1ST TRANCHE", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"2ND TRANCHE/RE-ENLISTMENT", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"FOR MEDICAL", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"EXPIRED ETE", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"ANCOC", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"BNCOC", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"SMC", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"BMT", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"CGSC", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"BAFOC", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PRIORITY COURSES", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"BY UNIT", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"SOT", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"2ND ETAD", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"1ST ETAD", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PROVISIONAL", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"OFFICER", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"ENLISTED PERSONNEL", None))
    # retranslateUi

