from PySide6.QtWidgets import *
from PySide6.QtCore import *
from Pelota import *
from PelotaLetra import PelotaLetra
from PelotaNumero import PelotaNumero
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Práctica 8 - Sorteo UAM")

        self.__form = QFormLayout()
        self.__identificador = QLineEdit()
        self.__nombre = QLineEdit()
        self.__form.addRow(QLabel("Identificador: "), self.__identificador)
        self.__form.addRow(QLabel("Nombre: "), self.__nombre)

        self.__botonLetra = QPushButton("Pelota Letra")
        self.__botonNumero = QPushButton("Pelota Número")
        self.__etLetra = QLabel("Premio Letra")
        self.__etNumero = QLabel("Premio Número")
        self.__calcularPremio = QPushButton("---PREMIO---")
        self.__calcularPremio.setProperty("class", "botonPremio")
        self.__etPremio = QLabel("Premio")
        self.__guardar = QPushButton("Guardar")
        self.__carga = QLabel("Archivo guardado")
        self.__carga.setObjectName("_carga")
        self.__mostrar = QPushButton("Mostrar premios")
        self.__etMostrar = QLabel()

        self.__grid = QGridLayout()
        self.__grid.addLayout(self.__form, 0, 0, 1, 2)
        self.__grid.addWidget(self.__botonLetra, 1, 0)
        self.__grid.addWidget(self.__etLetra, 1, 1)
        self.__grid.addWidget(self.__botonNumero, 2, 0)
        self.__grid.addWidget(self.__etNumero, 2, 1)
        self.__grid.addWidget(self.__calcularPremio, 3, 0, 1, 2)
        self.__grid.addWidget(self.__etPremio, 4, 0, 2, 2)
        self.__grid.addWidget(self.__guardar, 6, 0, 1, 2)
        self.__grid.addWidget(self.__carga, 7, 0, 1, 2)
        self.__grid.addWidget(self.__mostrar, 0, 3, 2, 2)
        self.__grid.addWidget(self.__etMostrar, 2, 3, 4, 2)

        widget_principal = QWidget()
        widget_principal.setLayout(self.__grid)

        ####### Agregar conexiones a Slots ######
        self.__botonLetra.clicked.connect(self.premioLetra)
        self.__botonNumero.clicked.connect(self.premioNumero)
        self.__calcularPremio.clicked.connect(self.decifraPremio)
        #########################################

        self.resize(800, 400)
        self.setCentralWidget(widget_principal)

    @Slot()
    def premioLetra(self):
        id = self.__identificador.text().strip()
        name = self.__nombre.text().strip()

        if not all([id, name]):
            QMessageBox.warning(
                self,
                "Campos vacíos",
                "Por favor llene todos los campos antes de enviar.\n",
            )
            return

        pelota_letra = PelotaLetra(id, name)
        premio_text = str(pelota_letra)
        self.__etLetra.setText(premio_text)

    @Slot()
    def premioNumero(self):
        id = self.__identificador.text().strip()
        name = self.__nombre.text().strip()

        if not all([id, name]):
            QMessageBox.warning(
                self,
                "Campos vacíos",
                "Por favor llene todos los campos antes de enviar.\n",
            )
            return

        pelota_numero = PelotaNumero(id, name)
        print(pelota_numero)
        premio_text = str(pelota_numero)
        self.__etNumero.setText(premio_text)

    @Slot()
    def decifraPremio(self):
        premio_msg = PelotaLetra.decifrarPremio()

    @Slot()
    def guardar(self):
        pass

    @Slot()
    def mostrar(self):
        pass


if __name__ == "__main__":
    app = QApplication([])

    ####### Agregar estilos QSS ######

    ##################################

    ventana = MainWindow()
    ventana.show()
    app.exec()
