import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QFrame,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt


class ExpandableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.expand_button = QPushButton("Expand", self)
        self.expand_button.clicked.connect(self.toggle_expansion)

        self.content = QWidget(self)  # The content that will expand
        self.content.setVisible(False)

        # Add components to layout
        self.layout.addWidget(self.expand_button)
        self.layout.addWidget(self.content)

    def toggle_expansion(self):
        self.content.setVisible(not self.content.isVisible())
        if self.content.isVisible():
            self.expand_button.setText("Collapse")
        else:
            self.expand_button.setText("Expand")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget with a scroll area
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        self.scroll_area.setWidget(self.scroll_content)

        # Add the scroll area to the central widget
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.scroll_area)

        # Add expandable widgets to the scroll area
        for i in range(23):
            self.scroll_layout.addWidget(ExpandableWidget())

        # Make sure the scroll area behaves properly
        self.scroll_content.adjustSize()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
