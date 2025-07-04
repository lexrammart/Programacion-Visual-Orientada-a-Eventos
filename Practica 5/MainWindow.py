from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QGridLayout, QPushButton, QSizePolicy, QLineEdit)
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QSize
import sys


class Keys():
    def __init__(self):
    
        self.boton_0 = QPushButton("0")
        self.boton_1 = QPushButton("1")
        self.boton_2 = QPushButton("2")
        self.boton_3 = QPushButton("3")
        self.boton_4 = QPushButton("4")
        self.boton_5 = QPushButton("5")
        self.boton_6 = QPushButton("6")
        self.boton_7 = QPushButton("7")
        self.boton_8 = QPushButton("8")
        self.boton_9 = QPushButton("9") 
        
        self.boton_clear = QPushButton("C")
        self.boton_addition = QPushButton("+")
        self.boton_substraction = QPushButton("-")
        self.boton_equals = QPushButton("=")
        
        self.boton_texto = QLineEdit()
        solo_enteros = QIntValidator(0, 999_999)   # rango opcional
        self.boton_texto.setValidator(solo_enteros)
        

class MainWindow(QMainWindow):
    
    # constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
    
        self.setWindowTitle("Calculadora")

        # layout
        layout = QGridLayout()
        layout.setSpacing(8)

        # botones
        boton = Keys()
        layout.addWidget(boton.boton_texto, 0, 0, 1, 3)
        layout.addWidget(boton.boton_clear, 0, 4, 1, 1)
        layout.addWidget(boton.boton_0, 4, 0, 1, 1)
        layout.addWidget(boton.boton_1, 1, 0, 1, 1)
        layout.addWidget(boton.boton_2, 1, 1, 1, 1)
        layout.addWidget(boton.boton_3, 1, 2, 1, 1)
        layout.addWidget(boton.boton_4, 2, 0, 1, 1)
        layout.addWidget(boton.boton_5, 2, 1, 1, 1)
        layout.addWidget(boton.boton_6, 2, 2, 1, 1)
        layout.addWidget(boton.boton_7, 3, 0, 1, 1)
        layout.addWidget(boton.boton_8, 3, 1, 1, 1)
        layout.addWidget(boton.boton_9, 3, 2, 1, 1)
        layout.addWidget(boton.boton_equals, 4, 1, 1, 2)
        layout.addWidget(boton.boton_addition, 1, 4, 2, 1)
        layout.addWidget(boton.boton_substraction, 3, 4, 2, 1)
        
        boton.boton_addition.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        boton.boton_substraction.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        
    

        # main widget
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        self.setFixedSize(QSize(200, 120))
        self.setCentralWidget(main_widget)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec())
    