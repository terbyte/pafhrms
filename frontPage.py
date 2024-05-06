from PySide6.QtWidgets import QMainWindow,QMenu, QFileDialog
from PySide6.QtGui import QAction
# from ui_index import Ui_MainWindow
from ui_index import Ui_MainWindow



class MySideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")




        #HIDING ALL THE DROPDOWNS ON DEFAULT
        def hideEmall():
            self.afsc_monitoring_dropdown.setHidden(True)
            self.elinstschooling_dropdown.setHidden(True)
            self.officerschooling_dropdown.setHidden(True)
            self.promotion_dropdown.setHidden(True)
            self.reenlistmen_dropdown.setHidden(True)
            self.schooling_dropdown.setHidden(True)
            self.seniority_dropdown.setHidden(True)
            self.placement_dropdown.setHidden(True)
            self.etad_SOT_dropdown.setHidden(True)
            self.attrition_dropdown.setHidden(True)

        
        # def uncheck_all():

            
        


        hideEmall()


        self.personnel_recordsbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.personnel_records_page))
        self.inactivepersonnel_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Inactive_personnel_page_01))
        self.palcement_offr_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Placement_page_officer_page))
        self.placementenlist_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.placementpage_enlist_page))
        self.palcement_offr_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Placement_page_officer_page))
        self.personnel_recordsbtn.clicked.connect(hideEmall)

    





        

