import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QFormLayout, QGridLayout,
    QLineEdit, QTextEdit, QGroupBox,
    QVBoxLayout, QRadioButton, QSizePolicy
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Práctica 6")
        
        self.resize(400, 350)
        self.setMinimumSize(300, 250)
        self.setMaximumSize(600, 500)

        
        central = QWidget()
        main_layout = QFormLayout(central)
        main_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.setCentralWidget(central)

       
        self.matricula_edit = QLineEdit()
        main_layout.addRow("Matrícula:", self.matricula_edit)

        self.nombre_edit = QLineEdit()
        main_layout.addRow("Nombre:", self.nombre_edit)

        self.apellidos_edit = QLineEdit()
        main_layout.addRow("Apellidos:", self.apellidos_edit)

       
        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)

        
        unidad_box = QGroupBox("Unidad:")
        unidad_box.setAlignment(Qt.AlignHCenter)
        unidad_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        u_layout = QVBoxLayout(unidad_box)
        for texto in ("Azc", "Xoc", "Izt"):
            u_layout.addWidget(QRadioButton(texto))
        grid.addWidget(unidad_box, 0, 0)

        
        division_box = QGroupBox("División:")
        division_box.setAlignment(Qt.AlignHCenter)
        division_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        d_layout = QVBoxLayout(division_box)
        for texto in ("CBI", "CSH", "CyAD"):
            d_layout.addWidget(QRadioButton(texto))
        grid.addWidget(division_box, 0, 1)

        
        main_layout.addRow(grid)

        
        self.asunto_edit = QLineEdit()
        main_layout.addRow("Asunto:", self.asunto_edit)

        self.mensaje_edit = QTextEdit()
        main_layout.addRow("Mensaje:", self.mensaje_edit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())