from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Slot
from Cuadrado import Cuadrado

def make_shape_box(name, fields):
    box = QWidget()
    vbox = QVBoxLayout()
    box.setLayout(vbox)
    vbox.addWidget(QLabel(name))
    for field in fields:
        vbox.addWidget(QLabel(field.capitalize()))
        line_edit = QLineEdit()
        vbox.addWidget(line_edit)
        setattr(box, f"{field}_edit", line_edit)
    btn = QPushButton("Calcular Área")
    vbox.addWidget(btn)
    setattr(box, "button", btn)
    result_lbl = QLabel("")
    vbox.addWidget(result_lbl)
    setattr(box, "result_label", result_lbl)
    return box

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Áreas")
        layout = QVBoxLayout()
        self.setLayout(layout)

        square_box = make_shape_box("Cuadrado", ["color", "lado"])

        # Referencias a los widgets del cuadro "Cuadrado"
        self._color1 = square_box.color_edit
        self._lado1  = square_box.lado_edit
        self._result1 = square_box.result_label
        square_box.button.clicked.connect(self.squareArea)

        layout.addWidget(square_box)

    @Slot()
    def squareArea(self):
        """Calcula el área del cuadrado y muestra el resultado."""
        try:
            lado = float(self._lado1.text())
            square = Cuadrado(self._color1.text(), lado)
            self._result1.setText(str(square))
        except ValueError:
            self._result1.setText("Error: ingresa un número válido en Lado")