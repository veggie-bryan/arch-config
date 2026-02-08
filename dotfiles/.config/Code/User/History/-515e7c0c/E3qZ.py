from screens.boot_screen import BootScreen
from screens.preview_screen import PreviewScreen
from screens.menu_screen import MenuScreen

class ScreenManager:
    def __init__(self, start_screen):
        self.screens = {
            "boot": BootScreen(self),
            "preview": PreviewScreen(self),
            "menu": MenuScreen(self)
        }
        self.current_screen = self.screens[start_screen]

    def change_screen(self, name):
        self.current.on_exit()
        self.current = self.screens[name]
        self.current.on_enter()

    def handle_event(self, event):
        self.current.handle_event(event)

    def update(self):
        self.current.update()

    def draw(self):
        self.current.draw()
