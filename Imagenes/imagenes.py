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

        current_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_path, "imagen_python.jpg")

        self._pixmap = QPixmap(image_path)

        if self._pixmap.isNull():
            print("Error al cargar la imagen")
        else:
            self._label = QLabel()
            self._label.setPixmap(self._pixmap)
            self._label.adjustSize()

            self.setCentralWidget(self._label)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()
    app.exec()
