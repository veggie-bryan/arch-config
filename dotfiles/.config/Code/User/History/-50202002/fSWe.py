# camera/mock_camera.py

import os
from camera.camera_base import CameraBase

class MockCamera(CameraBase):
    def __init__(self):
        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.last_image_path = os.path.join(
            project_root,
            "assets",
            "totoroNightSky.png"
        )

    def get_preview(self):
        return self.last_image_path

    def capture(self):
        print("Mock capture")
        return self.last_image_path

    def get_last_image(self):
        return self.last_image_path
