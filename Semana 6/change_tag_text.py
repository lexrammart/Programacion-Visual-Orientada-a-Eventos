import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QLabel,
    QVBoxLayout, QWidget, 
)
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal y Slot 2")
        
        self._textInput = QLineEdit()
        self._boton = QPushButton("Change tag text")
        self._tag = QLabel("Texto")
        
        self._boton.clicked.connect(self.changeText)
        # self._textInput.textChanged.connect(self._tag.setText)


        layout = QVBoxLayout()
        layout.addWidget(self._textInput)
        layout.addWidget(self._boton)
        layout.addWidget(self._tag)
        
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
    
    @Slot()
    def changeText(self):
        self._tag.setText(self._textInput.text())    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
