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
        self._tag = QLabel("Texto")
        
        
        self._textInput.textChanged.connect(self._tag.setText)


        layout = QVBoxLayout()
        layout.addWidget(self._textInput)
        layout.addWidget(self._tag)
        
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

