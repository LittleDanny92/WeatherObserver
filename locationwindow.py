from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from center import center

class LocationWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Location")
        self.setFixedSize(250,140)
        center(self.frameGeometry())

        self.init_gui()

    def init_gui(self):
        
        dialog_layout = QVBoxLayout()
        self.setLayout(dialog_layout)

        self.write_location_label = QLabel("Weather location", self)
        self.write_location_label.setFont(QFont("Arial", 12))
        self.write_location_label.setFixedSize(150,30)
        self.write_location_label.setAlignment(Qt.AlignLeft)
        dialog_layout.addWidget(self.write_location_label)

        self.location_edit = QLineEdit()
        self.location_edit.setFont(QFont("Arial", 11))
        self.location_edit.setMaxLength(80)
        self.location_edit.setFixedHeight(30)
        dialog_layout.addWidget(self.location_edit)

        self.accept_button = QPushButton("Accept")
        self.accept_button.setFixedSize(90,40)
        dialog_layout.addWidget(self.accept_button)

        self.accept_button.setDefault(True)
        self.accept_button.clicked.connect(self.accept)

        dialog_layout.setAlignment(self.accept_button, Qt.AlignRight)

    def get_location(self):
        location = self.location_edit.text().title()
        self.location_edit.setText("")
        return location

