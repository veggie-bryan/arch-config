# main.py

import sys
from PyQt6.QtWidgets import QApplication
from screen_manager import ScreenManager
from camera.mock_camera import MockCamera
from gpio_listener import GPIOListener

def main():
    app = QApplication(sys.argv)

    camera = MockCamera()
    manager = ScreenManager(camera)

    gpio = GPIOListener()
    app.installEventFilter(gpio)

    gpio.event_signal.connect(manager.handle_event)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
