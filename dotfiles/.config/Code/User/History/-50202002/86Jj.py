# Fake camera inputs for testing purposes

from camera.camera_base import CameraBase

class MockCamera(CameraBase):
    def __init__(self):
        self.last_image = "assets/totoroNightSky.jpg"

    def get_preview(self):
        return self.last_image_path
    
    def capture(self):
        print("Mock capture")
        return self.last_image_path
    
    def get_last_image(self):
        return self.last_image_path
    