from pathlib import Path
from datetime import datetime
import subprocess

PHOTOS_DIR = Path.home() / "photos"

def ensure_photos_dir():
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

def new_photo_path():
    now = datetime.now()

    timestamp = now.strftime("%Y%m%d_%H%M%S")
    milliseconds = int(now.microsecond / 1000)

    filename = f"{timestamp}_{milliseconds:03d}.jpg"

    return PHOTOS_DIR / filename

def capture_photo():
    ensure_photos_dir()
    output_path = new_photo_path()

    cmd = [
        "rpicam-still",
        "-o", str(output_path),
        "--nopreview",
        "-t", "1",
        "--quality", "92",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(
            "Camera capture failed:\n"
            + result.stderr
        )
    
    return output_path