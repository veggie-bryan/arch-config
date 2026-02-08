from screens.screen_base import Screen
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class PreviewScreen(Screen):
    def __init__(self, managerm, camera):
        self.manager = manager
        self.camera = camera
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def on_enter(self):
        self.update_image()
        self.label.show()

    def on_exit(self):
        self.label.hide()

    def update_image(self):
        path = self.camera.get_preview()
        pixmap = QPixmap(path)
        self.label.setPixmap(pixmap.scaled(
            640, 480,
            Qt.AspectRatioMode.KeepAspectRatio
        ))

    def handle_event(self, event):
        if event == "SHUTTER":
            self.camera.capture()
            self.update_image()