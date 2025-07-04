import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton
)
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal y Slot")
        
        self._boton = QPushButton("Un botón")
        self._boton.setCheckable(True)
        self._boton.clicked.connect(self.clickBoton)
        self._boton.clicked.connect(self.botonCheck)
        self.setCentralWidget(self._boton)

    @Slot()
    def clickBoton(self):
        self._boton.setText("Realizaste un click.")
        print("Se realizó un click.")

    @Slot(bool)
    def botonCheck(self, checked):
        print(checked)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    