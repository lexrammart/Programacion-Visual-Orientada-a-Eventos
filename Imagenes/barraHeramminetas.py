from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de Herramientas")

        self._toolbar = QToolBar("Barra de Herraminetas")
        self._label = QLabel("Content")
        self._label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self._label)

        self.addToolBar(self._toolbar)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()
    app.exec()
