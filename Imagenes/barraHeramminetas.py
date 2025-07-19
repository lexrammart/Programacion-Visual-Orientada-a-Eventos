from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de Herramientas")
        self.setFixedSize(500, 200)

        self._toolbar = QToolBar("Barra de Herraminetas")

        current_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_path, "cloud-download.ico")
        down_icon = QIcon(icon_path)

        self._accion = QAction(down_icon, "Just a Click", self)  # Create an action
        self._toolbar.addAction(self._accion)  # Add action to toolbar
        self._accion.setStatusTip("Estado de la acción")
        self.setStatusBar(QStatusBar(self))  # Set status bar

        self._label = QLabel("Content")
        self._label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self._label)

        self.addToolBar(self._toolbar)

        self._accion.triggered.connect(self.clicking)

    @Slot()
    def clicking(self):
        print("You're clicking")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()
    app.exec()
