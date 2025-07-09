from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Slot
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ventana
        self.setWindowTitle("Práctica 7")
        self.resize(800, 500)

        # Layouts principales
        grid_layout = QGridLayout()
        form_layout = QFormLayout()
        form_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        form_layout.setLabelAlignment(Qt.AlignLeft)
        vbox_layout = QVBoxLayout()

        # Columna izquierda 
        self.input_date = QLineEdit()
        self.input_date.setFixedSize(250, 30)

        self.input_matricula = QLineEdit()
        self.input_matricula.setFixedSize(250, 30)

        self.input_name = QLineEdit()
        self.input_name.setFixedSize(250, 30)

        self.input_message = QTextEdit()
        self.input_message.setFixedSize(250, 200)

        self.send_key = QPushButton("Enviar")
        self.send_key.setFixedSize(300, 40)
        self.send_key.clicked.connect(self.enviar_mensaje)

        # Añadir campos al formulario
        form_layout.addRow("Fecha:", self.input_date)
        form_layout.addRow("Matrícula", self.input_matricula)
        form_layout.addRow("Nombre:", self.input_name)
        form_layout.addRow("Mensaje:", self.input_message)
        form_layout.addRow("", self.send_key)

        # Columna derecha
        self.label_title = QLabel("MENSAJES UAM")
        self.label_title.setFixedSize(300, 40)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.area_mensajes = QLabel()
        self.area_mensajes.setFixedSize(300, 400)
        self.area_mensajes.setWordWrap(True)

        # Layout vertical derecho
        vbox_layout.addWidget(self.label_title)
        vbox_layout.addWidget(self.area_mensajes)
        vbox_layout.setAlignment(Qt.AlignLeft)

        # Integrar layouts al grid
        grid_layout.addLayout(form_layout, 0, 0)
        grid_layout.addLayout(vbox_layout, 0, 1)

        # Contenedor principal
        container = QWidget()
        container.setLayout(grid_layout)
        self.setCentralWidget(container)

    #  Slots
    @Slot()
    def enviar_mensaje(self):
        date       = self.input_date.text().strip()
        matricula  = self.input_matricula.text().strip()
        name       = self.input_name.text().strip()
        message    = self.input_message.toPlainText().strip()

        if not all([date, matricula, name, message]):
            QMessageBox.warning(
                self,
                "Campos vacíos",
                "Por favor llena todos los campos antes de enviar.\n"
            )
            return

        texto = (
            f"Fecha: {date}\n"
            f"Matrícula: {matricula}\n"
            f"Nombre: {name}\n"
            f"Mensaje: {message}\n"
            "----------\n"
        )
        self.area_mensajes.setText(self.area_mensajes.text() + texto)

        # Limpiar campos
        self.input_date.clear()
        self.input_matricula.clear()
        self.input_name.clear()
        self.input_message.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())