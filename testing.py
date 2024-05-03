import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt

# Create a subclass of QPushButton to implement hover events
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



# Create a simple application with a main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hover Event Example")
        
        # Create a HoverButton instance
        self.button = HoverButton("Hover over me", self)
        self.setCentralWidget(self.button)
        

# Main block to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
