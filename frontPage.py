from PySide6.QtWidgets import QMainWindow,QMenu
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow


class MySideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")


        #HIDING ALL THE DROPDOWNS ON DEFAULT
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



        self.personnel_recordsbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        
        self.inactivepersonnel_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))




        

