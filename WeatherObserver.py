# -*- coding: utf-8 -*-

import sys
import os
from PyQt5 import (
    QtWidgets,
    QtCore,
    
    )
    
from mainwindow import MainWindow   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    try:
        css_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "format.css")
        css_file = QtCore.QFile(css_path)
        if css_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            style = QtCore.QTextStream(css_file).readAll()
            css_file.close()
        app.setStyleSheet(style)
    except:
        pass

    mainWindow = MainWindow()
    try:
        mainWindow.show()
    except:
        pass
    sys.exit(app.exec())
