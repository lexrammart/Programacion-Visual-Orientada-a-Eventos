# clase QPixmap
# se debe agregar a un ConnectionAbortedError

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu bar")

        self._menu_Archivo = QMenu("Archivo", self)

        self._menu_bar = self.menuBar()

        self._menu_bar.addMenu(self._menu_Archivo)
        self._menu_options = QMenu("Opcion", self)
        self._menu_Archivo.addMenu(self._menu_options)

        self._option1 = QAction("Opción 1", self)
        self._option2 = QAction("Opción 2", self)
        self._option3 = QAction("Opción 3", self)

        self._menu_options.addAction(self._option1)
        self._menu_options.addAction(self._option2)
        self._menu_options.addAction(self._option3)

        self.setCentralWidget(self._menu_bar)
        self._option1.triggered.connect(self.clicking)

    @Slot()
    def clicking(self):
        print("You're clicking")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()
    app.exec()
