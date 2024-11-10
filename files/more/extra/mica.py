import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from win32mica import ApplyMica

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Mica Effect Example")
        self.setWindowFlags(self.windowFlags())
        ApplyMica(self.winId(), True)  # Enable dark mode

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())