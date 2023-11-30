from PyQt5 import (
    QtWidgets,
    QtCore
)

from center import center
from pdf2image import convert_from_path

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF2JPG")
        self.setFixedSize(400,150)
        center(self.frameGeometry())

        self.init_gui()

    def init_gui(self):
        
        main = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout()
        main.setLayout(grid)
        self.setCentralWidget(main)

        grid.setSpacing(15)

        self.find_pdf_button = QtWidgets.QPushButton("PDF to convert:")
        self.find_pdf_button.setFixedSize(100,40)
        grid.addWidget(self.find_pdf_button, 0,0,1,2, QtCore.Qt.AlignLeft)

        self.pdf_path_edit = QtWidgets.QLineEdit()
        self.pdf_path_edit.setMaxLength(200)
        self.pdf_path_edit.setFixedHeight(40)
        grid.addWidget(self.pdf_path_edit, 0,2,1,3)

        self.convert_pdf_button = QtWidgets.QPushButton("Convert PDF")
        self.convert_pdf_button.setFixedSize(100,40)
        grid.addWidget(self.convert_pdf_button, 1,0,1,2)

        self.form_reset_button = QtWidgets.QPushButton("Reset the form")
        self.form_reset_button.setFixedSize(100,40)
        grid.addWidget(self.form_reset_button, 1,2,1,2)

        self.find_pdf_button.clicked.connect(self.find_pdf)
        self.convert_pdf_button.clicked.connect(self.execute_convertion)
        self.form_reset_button.clicked.connect(self.reset_form)

        self.error_msg_box = QtWidgets.QMessageBox()
        self.error_msg_box.setWindowTitle("Error")
        self.error_msg_box.setIcon(QtWidgets.QMessageBox.Warning)

        self.info_msg_box = QtWidgets.QMessageBox()
        self.info_msg_box.setWindowTitle("Information")
        self.info_msg_box.setIcon(QtWidgets.QMessageBox.Information)

    def find_pdf(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self,"Open File", "", "PDF (*.pdf);; All Files (*)")

        if file_path:
            self.pdf_path_edit.setText(file_path)
        
    def convert_pdf(self, pdf_path):
        return convert_from_path(pdf_path, fmt = "jpg")

    def execute_convertion(self):
        if self.pdf_path_edit.text().endswith(".pdf"):
            try:
                jpg_images = self.convert_pdf(self.pdf_path_edit.text())
                self.save_jpg(jpg_images)
            except:
                self.error_msg_box.setText("The creation of JPG failed.")
                self.error_msg_box.exec()
            else:
                self.info_msg_box.setText("The PDF was successfully converted.")
                self.info_msg_box.exec()
        else:
            self.info_msg_box.setText("The PDF file was not chosen.")
            self.info_msg_box.exec()
    
    def save_jpg(self, jpgs):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self,"Save jpg File", "", "Images (*.jpg);; All Files (*)")
        if file_path:
            file_path = file_path.rstrip(".jpg")
            for i,jpg in enumerate(jpgs):
                jpg.save(f"{file_path}_{i+1}.jpg")            
    
    def reset_form(self):
        self.pdf_path_edit.clear()
