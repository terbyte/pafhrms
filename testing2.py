import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow,QMenu
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow


class HoverButton(QPushButton):
    # This method is called when the mouse pointer enters the button
    def enterEvent(self, event):
        # Change the button's background color to a lighter shade
        super().enterEvent(event)
        print("entered")
    
    # This method is called when the mouse pointer leaves the button
    def leaveEvent(self, event):
        # Revert the button's background color to the original
        super().leaveEvent(event)
        print("left")



class MySideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")


        self.personnel_recordsbtn = HoverButton(self.personnel_recordsbtn)



def hidealldropdowns(self):
    self.afsc_monitoring_dropdown.setHidden(True)
    self.elinstschooling_dropdown.setHidden(True)
    self.officerschooling_dropdown.setHidden(True)
    self.promotion_dropdown.setHidden(True)
    self.reenlistmen_dropdown.setHidden(True)
    self.schooling_dropdown.setHidden(True)
    self.seniority_dropdown.setHidden(True)
    self.placement_dropdown.setHidden(True)
    self.etad_SOT_dropdown.setHidden(True)


app = QApplication(sys.argv)


window =MySideBar()


window.show()
app.exec()