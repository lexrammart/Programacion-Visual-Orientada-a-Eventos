from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QMainWindow, QGridLayout, QSizePolicy)
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    
    # constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout Example")

        # botones
        button1 = QPushButton("Botón 1")
        button2 = QPushButton("Botón 2")
        button3 = QPushButton("Botón 3")
        button4 = QPushButton("Botón 4")
        button5 = QPushButton("Botón 5")
        button5.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        # layout
        layout = QGridLayout()
        # layout.setContentsMargins(10, 10, 10, 10)   # opcional, solo para estética
        layout.setSpacing(5)

        layout.addWidget(button3, 0, 1, 1, 2)   # fila 0, col 1, ocupa 1 fila × 2 columnas
        layout.addWidget(button5, 0, 3, 2, 2)   # fila 0, col 3, ocupa 2 filas × 2 cols
        layout.addWidget(button1, 1, 0, 1, 2)   # fila 1, col 0, ocupa 1 fila × 2 cols
        layout.addWidget(button4, 2, 1, 1, 3)   # fila 2, col 1, ocupa 1 fila × 3 cols
        layout.addWidget(button2, 3, 0, 1, 5)   # fila 3, col 0, ocupa 1 fila × 5 cols
        
        main_widget = QWidget()
        main_widget.setLayout(layout)
        
        self.setFixedSize(QSize(200, 100))
        self.setCentralWidget(main_widget)
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    