# main.py

import sys
from PyQt6.QtWidgets import QApplication

from camera.mock_camera import MockCamera
from screen_manager import ScreenManager
from gpio_listener import GPIOListener
from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    camera = MockCamera()
    manager = ScreenManager(camera, window)

    gpio = GPIOListener()
    app.installEventFilter(gpio)
    gpio.event_signal.connect(manager.handle_event)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
