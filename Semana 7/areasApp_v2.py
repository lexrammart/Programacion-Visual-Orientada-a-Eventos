import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Slot
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cuadrado y Rectángulo: Área")
        self.setFixedSize(500, 200)

        # layout
        grid_layout = QGridLayout()
        form_layout1 = QFormLayout()
        form_layout2 = QFormLayout()

        form_layout1.setFormAlignment(Qt.AlignLeft)
        form_layout2.setFormAlignment(Qt.AlignLeft)

        # labels & widgets
        self.sqr_area_button = QPushButton("Calcular Área")
        self.rec_area_button = QPushButton("Calcular Área")

        # columna derecha
        form_layout1.addRow("", QLabel("Cuadrado"))
        form_layout1.addRow("Color: ", QLineEdit())
        form_layout1.addRow("Lado: ", QLineEdit())
        form_layout1.addRow("", self.sqr_area_button)

        # columna izquierda
        form_layout2.addRow("", QLabel("Rectángulo"))
        form_layout2.addRow("Color: ", QLineEdit())
        form_layout2.addRow("Lado: ", QLineEdit())
        form_layout2.addRow("Lado: ", QLineEdit())
        form_layout2.addRow("", self.rec_area_button)

        # otro layout
        grid_layout.addLayout(form_layout1, 0, 0)
        grid_layout.addLayout(form_layout2, 0, 1)

        # main widget
        main_widget = QWidget()
        main_widget.setLayout(grid_layout)
        self.setCentralWidget(main_widget)

    @Slot()
    def calularArea(self):

        pass


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
