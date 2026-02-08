from screens.preview_screen import PreviewScreen

class ScreenManager:
    def __init__(self, camera):
        self.camera = camera

        self.screens = {
            "preview": PreviewScreen(self, camera),
        }

        self.current = self.screens["preview"]
        self.current.on_enter()

    def change_screen(self, name):
        self.current.on_exit()
        self.current = self.screens[name]
        self.current.on_enter()

    def handle_event(self, event):
        self.current.handle_event(event)