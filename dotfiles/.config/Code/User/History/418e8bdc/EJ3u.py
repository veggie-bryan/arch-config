from PyQt6.QtCore import QObject, pyqtSignal

class GPIOListener(QObject):
    event_signal = pyqtSignal(str)

    def keyPressEvent(self, event):
        key = event.key()

        if key == 32: # Spacebar
            self.gpio_event.emit("SHUTTER")