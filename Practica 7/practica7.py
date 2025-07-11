from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Slot
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Práctica 7")
        self.resize(800, 500)

        # Layouts
        grid_layout = QGridLayout()
        form_layout = QFormLayout()
        vbox_layout = QVBoxLayout()

        form_layout.setFormAlignment(Qt.AlignLeft)
        form_layout.setLabelAlignment(Qt.AlignLeft)

        # Columna izquierda
        self.input_fecha = QLineEdit()
        self.input_matricula = QLineEdit()
        self.input_nombre = QLineEdit()
        self.input_mensaje = QLineEdit()

        self.input_fecha.setFixedSize(250, 30)
        self.input_matricula.setFixedSize(250, 30)
        self.input_nombre.setFixedSize(250, 30)
        self.input_mensaje.setFixedSize(250, 30)

        self.send_buton = QPushButton("Enviar")
        self.send_buton.setFixedSize(300, 40)
        self.send_buton.clicked.connect(self.send_msg)

        # formulario datos
        form_layout.addRow("Fecha: ", self.input_fecha)
        form_layout.addRow("Matricula: ", self.input_matricula)
        form_layout.addRow("Nombre: ", self.input_nombre)
        form_layout.addRow("Mensaje: ", self.input_mensaje)
        form_layout.addRow("", self.send_buton)

        # columna derecha:
        self.label_title = QLabel("MENSAJES UAM")
        self.label_title.setFixedSize(300, 40)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.label_mensaje = QLabel()
        self.label_mensaje.setFixedSize(300, 400)
        self.label_mensaje.setWordWrap(True)

        vbox_layout.addWidget(self.label_title)
        vbox_layout.addWidget(self.label_mensaje)

        # otro layout
        grid_layout.addLayout(form_layout, 0, 0)
        grid_layout.addLayout(vbox_layout, 0, 1)

        # contenedor principal
        main_widget = QWidget()
        main_widget.setLayout(grid_layout)
        self.setCentralWidget(main_widget)

    @Slot()
    def send_msg(self):
        fecha = self.input_fecha.text().strip()
        matricula = self.input_matricula.text().strip()
        nombre = self.input_nombre.text().strip()
        mensaje = self.input_mensaje.text().strip()

        if not all([fecha, matricula, nombre, mensaje]):
            QMessageBox.warning(
                self,
                "Campos vacíos",
                "Por favor llene todos los campos antes de enviar.\n",
            )
            return

        msg_text = (
            f"Fecha :{fecha}\n"
            f"Matricula :{matricula}\n"
            f"Nombre :{nombre}\n"
            f"Mensaje :{mensaje}\n"
            "------------------\n"
        )

        self.label_mensaje.setText(self.label_mensaje.text() + msg_text)

        # limpiar campos
        self.input_fecha.clear()
        self.input_nombre.clear()
        self.input_matricula.clear()
        self.input_mensaje.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
