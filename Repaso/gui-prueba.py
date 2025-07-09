from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Slot
import sys

class Widgts(QWidget):
    def __init__(self):
        super().__init__()

        # layout = QGridLayout(self)
        
        self.cuadrado_label = QLabel("Cuadrado")
        self.rectangulo_label = QLabel("Rectángulo")
        self.boton_area_sqr = QPushButton("Calcular área")
        self.boton_area_rec = QPushButton("Calcular área")
        self.mnsj_cuadrado = QLabel("La figura es de color blah tiene un lado de blah")
        self.mnsj_rectangulo = QLabel("La fugra es de color blah")
        self.mnsj_area_sqr = QLabel("Área: X")
        self.mnsj_area_rec = QLabel("Área: X")
        
        wdgts = [
            self.cuadrado_label,
            self.rectangulo_label,
            self.boton_area_sqr,
            self.boton_area_rec,
            self.mnsj_cuadrado,
            self.mnsj_rectangulo,
            self.mnsj_area_sqr,
            self.mnsj_area_rec
        ]
        
        box = ShapeBox(wdgts)
        layout = box.layoutExterno()
        self.setLayout(layout)
        

class ShapeBox:
    def __init__(self, widgets):
        # self.widgets = widgets
        self.cuadrado_label, self.rectangulo_label, self.boton_area_sqr, self.boton_area_rec, self.mnsj_cuadrado, self.mnsj_rectangulo, self.mnsj_area_sqr, self.mnsj_area_rec = widgets

    def layoutInterno(self):
        pass

    def layoutExterno(self):
        layout = QGridLayout()

        layout.addWidget(self.cuadrado_label, 0, 0)
        layout.addWidget(self.rectangulo_label, 0, 1)
        
        layout.addWidget(self.boton_area_sqr, 1, 0)
        layout.addWidget(self.boton_area_rec, 1, 1)
        
        layout.addWidget(self.mnsj_cuadrado, 2, 0)
        layout.addWidget(self.mnsj_rectangulo, 2, 1)
        
        layout.addWidget(self.mnsj_area_sqr, 3, 0)
        layout.addWidget(self.mnsj_area_rec, 3, 1)
        # Example: add widgets to layout
        # for i, widget in enumerate(self.widgets):
        #     layout.addWidget(widget, i, 0)
        
        return layout
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Área de Figuras")
        self.setFixedSize(500, 200)
        
        
        # main_widget = QWidget()
        self.setCentralWidget(Widgts())
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
    