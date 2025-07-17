import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self._layout = QHBoxLayout()

        self.boton1 = QPushButton("Botoncito")

        main_windget = QWidget()
        main_windget.setLayout(self._layout)
        self.setCentralWidget(main_windget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    archivoEstilos = os.path.join(ruta_actual, "estilos.qss")
    with open(archivoEstilos, "r") as f:
        qss = f.read()
    app.setStyleSheet(qss)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
