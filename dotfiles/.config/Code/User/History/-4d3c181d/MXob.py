# screens/preview_screen.py

from screens.screen_base import Screen
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class PreviewScreen(Screen):
    def __init__(self, manager, camera):
        self.manager = manager
        self.camera = camera

        self.widget = QLabel()
        self.widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def on_enter(self):
        self.update_image()
        self.manager.window.set_screen_widget(self.widget)

    def on_exit(self):
        pass

    def update_image(self):
        path = self.camera.get_preview()
        pixmap = QPixmap(path)

        if pixmap.isNull():
            print(f"Failed to load image: {path}")
            return

        self.widget.setPixmap(
            pixmap.scaled(
                self.manager.window.width(),
                self.manager.window.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

    def handle_event(self, event):
        if event == "SHUTTER":
            self.camera.capture()
            self.update_image()