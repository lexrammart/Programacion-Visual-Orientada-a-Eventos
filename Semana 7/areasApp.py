import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Slot
# from Figura2D import Figura2D
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo



def make_shape_box(title: str, fields: list[str]) -> QGroupBox:
    
    box = QGroupBox(title)
    box.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    # Layout interno
    vbox = QVBoxLayout(box)
    form = QFormLayout()
    form.setLabelAlignment(Qt.AlignLeft)
    form.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
    vbox.addLayout(form)

    # Inputs
    for field in fields:
        line_edit = QLineEdit()
        form.addRow(f"{field.capitalize()}:", line_edit)
        setattr(box, f"{field}_edit", line_edit)

    # Botón
    btn = QPushButton("Calcular Área")
    vbox.addWidget(btn)
    setattr(box, "button", btn)

    # Etiquetas de resultado
    result_lbl_a = QLabel("")
    result_lbl_b = QLabel("")
    grid = QGridLayout()
    grid.addWidget(result_lbl_a, 0, 0)
    grid.addWidget(result_lbl_b, 0, 1)
    vbox.addLayout(grid)
    setattr(box, "result_label_a", result_lbl_a)
    setattr(box, "result_label_b", result_lbl_b)
    

    return box
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera GUI - POO")
        self.resize(600, 300)

        # ── Secciones Cuadrado y Rectángulo ─────────────────────
        square_box = make_shape_box("Cuadrado", ["color", "lado"])
        self._color1 = square_box.color_edit
        self._lado1  = square_box.lado_edit
        self._result1_a = square_box.result_label_a
        self._result1_b = square_box.result_label_b
        square_box.button.clicked.connect(self.squareArea)

        rect_box   = make_shape_box("Rectángulo", ["color", "base", "altura"])
        self._color1 = rect_box.color_edit
        self._base   = rect_box.base_edit
        self._altura = rect_box.altura_edit
        self._result2_a = rect_box.result_label_a
        self._result2_b = rect_box.result_label_b
        rect_box.button.clicked.connect(self.rectangleArea) 

        # ── Layout principal: dos columnas ─────────────────────
        central = QWidget()
        hbox = QHBoxLayout(central)
        hbox.addWidget(square_box, 1)
        hbox.addWidget(rect_box, 1)
        self.setCentralWidget(central)
        
    @Slot()
    def squareArea(self):
        """Calcula el área del cuadrado y muestra el resultado."""
        try:
            lado = float(self._lado1.text())
            square = Cuadrado(self._color1.text(), lado)
            self._result1_a.setText(str(square))
        except ValueError:
            self._result1_a.setText("Error: ingresa un número válido en Lado")
    
    @Slot()
    def rectangleArea(self):
        """Calcula el área del rectángulo y muestra el resultado."""
        try:
            base = float(self._base.text())
            altura = float(self._altura.text())
            rectangle = Rectangulo(self._color1.text(), base, altura)
            self._result2_a.setText(str(rectangle))
        except ValueError:
            self._result2_a.setText("Error: ingresa un número valido en Base y Altura")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())