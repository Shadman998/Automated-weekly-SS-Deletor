import os
import time
from pathlib import Path

def delete_old_screenshots(folder_path, days=7):
    # Convert days to seconds: seconds * minutes * hours * days
    seconds_threshold = 60*60*24*days
    current_time = time.time()
    
    target_dir = Path(folder_path).expanduser().resolve()

    if not target_dir.exists():
        print("Path does not exist.")
        return

    for file_path in target_dir.iterdir():
        if file_path.is_file():
            # Get the time the file was last modified
            file_age = file_path.stat().st_mtime
            
            # Intuition: If (Now - FileTime) > 7 days, it's too old
            if (current_time - file_age) > seconds_threshold:
                try:
                    file_path.unlink() # This deletes the file
                    print(f"Deleted old file: {file_path.name}")
                except Exception as e:
                    print(f"Error deleting {file_path.name}: {e}")

if __name__ == "__main__":
    # Update this path to your actual ss folder
    SS_FOLDER_PATH = "C:/Users/USER/Pictures/Screenshots"
    delete_old_screenshots(SS_FOLDER_PATH)