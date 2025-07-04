import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)
from PySide6.QtCore import Slot
import random as rd


class GuessNumber(QWidget):
    def __init__(self):
        super().__init__()


        # Widgets
        self.__label_instrucciones = QLabel("Ingresa un número entre 1 y 20:")
        self.__entrada_usuario = QLineEdit()
        self.__boton_adivinar = QPushButton("Adivinar")
        self.__label_resultado = QLabel("")
        self.__label_number = QLabel("")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.__label_instrucciones)
        layout.addWidget(self.__entrada_usuario)
        layout.addWidget(self.__boton_adivinar)
        layout.addWidget(self.__label_resultado)
        layout.addWidget(self.__label_number)
        self.setLayout(layout)

        # Conexión de señal
        self.__boton_adivinar.clicked.connect(self.verificarNumero)

        # Configuración de la ventana
        self.setWindowTitle("Juego de Adivinar Número")
        self.setFixedWidth(300)

    @Slot()
    def verificarNumero(self):
        
        # Número secreto entre 1 y 100
        self.__secret_number = rd.randint(1, 20)
        
        try:
            numero_usuario = int(self.__entrada_usuario.text())
            if numero_usuario < self.__secret_number:
                self.__label_resultado.setText("El número secreto es mayor.")
                self.__label_number.setText("")
            elif numero_usuario > self.__secret_number:
                self.__label_resultado.setText("El número secreto es menor.")
                self.__label_number.setText("")
            else:
                self.__label_resultado.setText("¡Correcto! 🎉")
                self.__label_number.setText(f"El número era: {self.__secret_number}")
                # Deshabilita el botón para evitar más intentos
                self.__boton_adivinar.setEnabled(False)
        except ValueError:
            self.__label_resultado.setText("Por favor, ingresa un número válido.")
            self.__label_number.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuessNumber()
    window.show()
    sys.exit(app.exec())