# ui/main_window.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RasPi Camera")
        self.setFixedSize(640, 480)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def set_screen_widget(self, widget):
        # Remove old widget
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        # Add new screen widget
        self.layout.addWidget(widget)