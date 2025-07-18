from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        current_path = os.path.dirname(os.path.abspath(__file__))
        download_path = os.path.join(current_path, "download.png")

        # self._pixmap = QPixmap(download_path)

        self._icon = QIcon(download_path)
        self._button = QPushButton("Descarga")

        self._button.setIconSize(QSize(52, 52))
        self._button.setIcon(self._icon)
        self.setCentralWidget(self._button)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()
    app.exec()
