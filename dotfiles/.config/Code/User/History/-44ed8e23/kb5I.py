# camera.py

import os
import shutil
import time


class Camera:
    def __init__(self, preview_image_path, photos_dir="photos"):
        self.preview_image_path = preview_image_path
        self.photos_dir = photos_dir

        os.makedirs(self.photos_dir, exist_ok=True)

    def get_preview(self):
        """
        Return a path to an image suitable for preview.
        """
        return self.preview_image_path

    def capture(self):
        """
        Simulate taking a photo by copying the preview image
        into the photos directory with a timestamped name.
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"IMG_{timestamp}.png"
        dest_path = os.path.join(self.photos_dir, filename)

        shutil.copy(self.preview_image_path, dest_path)
        return dest_path

    def get_last_image(self):
        """
        Return the most recently captured image path,
        or None if no images exist.
        """
        images = [
            os.path.join(self.photos_dir, f)
            for f in os.listdir(self.photos_dir)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]

        if not images:
            return None

        return max(images, key=os.path.getctime)
