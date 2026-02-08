import os
import subprocess
from datetime import datetime
from pathlib import Path

PHOTOS_DIR = Path.home() / "photos"

def ensure_photos_dir():
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

def new_photo_path(ext=".jpg"):
    # Example: 20260111_123456_123.jpg
    now = datetime.now()
    stamp = now.strftime("%Y%m%d_%H%M%S")
    ms = int(now.microsecond / 1000)
    return PHOTOS_DIR / f"{stamp}_{ms:03d}{ext}"

def capture_photo():
    ensure_photos_dir()
    out = new_photo_path(".jpg")

    cmd = [
        "rpicam-still",
        "-o", str(out),
        "--nopreview",
        "-t", "1",             # capture immediately
        "--quality", "92",
        # keep these out at first; add later if you want:
        # "--width", "4056",
        # "--height", "3040",
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)

    if proc.returncode != 0:
        # Remove partial file if it exists
        if out.exists():
            try:
                out.unlink()
            except Exception:
                pass
        raise RuntimeError(
            "Capture failed.\n"
            f"Command: {' '.join(cmd)}\n"
            f"stderr:\n{proc.stderr.strip()}\n"
        )

    if not out.exists() or out.stat().st_size == 0:
        raise RuntimeError(f"Capture reported success, but file is missing/empty: {out}")

    return out

def list_photos(limit=10):
    if not PHOTOS_DIR.exists():
        return []
    photos = [p for p in PHOTOS_DIR.iterdir() if p.is_file() and p.suffix.lower() in (".jpg", ".jpeg", ".png")]
    photos.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return photos[:limit]

def latest_photo():
    photos = list_photos(limit=1)
    return photos[0] if photos else None

def main():
    ensure_photos_dir()
    print(f"Photo folder: {PHOTOS_DIR}\n")
    print("Commands:")
    print("  c  capture photo")
    print("  l  list latest photos")
    print("  p  print latest photo path")
    print("  q  quit")

    while True:
        try:
            cmd = input("\n[c/l/p/q] > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if cmd == "q":
            print("Bye.")
            break
        elif cmd == "c":
            try:
                path = capture_photo()
                print(f"Saved: {path}")
            except Exception as e:
                print(f"ERROR: {e}")
        elif cmd == "l":
            photos = list_photos(limit=10)
            if not photos:
                print("No photos found.")
            else:
                for i, p in enumerate(photos, 1):
                    print(f"{i:02d}. {p.name}")
        elif cmd == "p":
            p = latest_photo()
            print(p if p else "No photos found.")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
