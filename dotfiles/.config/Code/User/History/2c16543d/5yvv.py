# camera.py

import os
import shutil
import time

PHOTOS_DIR = "photos"
SUPPORTED_EXTENSIONS = (".png", ".jpg", ".jpeg")

camera_state = {
    "current_index": 0
}

def init_camera():
    if not os.path.exists(PHOTOS_DIR):
        os.makedirs(PHOTOS_DIR)

    photos = list_photos()
    if photos:
        camera_state["current_index"] = len(photos) - 1
    else:
        camera_state["current_index"] = 0


def list_photos():
    files = [
        f for f in os.listdir(PHOTOS_DIR)
        if f.lower().endswith(SUPPORTED_EXTENSIONS)
    ]
    files.sort()
    return files


def clamp_index(index):
    photos = list_photos()
    if not photos:
        return 0
    return max(0, min(index, len(photos) - 1))


def capture_photo(preview_image_path):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"IMG_{timestamp}.png"
    dest_path = os.path.join(PHOTOS_DIR, filename)

    shutil.copy(preview_image_path, dest_path)

    photos = list_photos()
    camera_state["current_index"] = len(photos) - 1

    return dest_path


def get_current_photo():
    photos = list_photos()
    if not photos:
        return None

    index = clamp_index(camera_state["current_index"])
    camera_state["current_index"] = index
    return os.path.join(PHOTOS_DIR, photos[index])


def next_photo():
    camera_state["current_index"] += 1
    camera_state["current_index"] = clamp_index(camera_state["current_index"])
    return get_current_photo()


def prev_photo():
    camera_state["current_index"] -= 1
    camera_state["current_index"] = clamp_index(camera_state["current_index"])
    return get_current_photo()


def delete_current_photo():
    path = get_current_photo()
    if path is None:
        return False

    os.remove(path)

    camera_state["current_index"] = clamp_index(camera_state["current_index"])
    return True