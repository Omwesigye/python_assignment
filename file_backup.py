import os
import shutil
import time
from datetime import datetime, timedelta

SOURCE_FOLDER = r'd:/python_tasks/source_folder'
BACKUP_FOLDER = r'd:/python_tasks/backup_folder'   
MODIFIED_WITHIN_MINUTES = 3

def backup_recent_files():
    now = datetime.now()
    cutoff = now - timedelta(minutes=MODIFIED_WITHIN_MINUTES)
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)
    for root, _, files in os.walk(SOURCE_FOLDER):
        for file in files:
            src_path = os.path.join(root, file)
            mtime = datetime.fromtimestamp(os.path.getmtime(src_path))
            if mtime >= cutoff:
                rel_path = os.path.relpath(src_path, SOURCE_FOLDER)
                dest_path = os.path.join(BACKUP_FOLDER, rel_path)
                dest_dir = os.path.dirname(dest_path)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.copy2(src_path, dest_path)
                print(f"Backed up: {src_path} -> {dest_path}")

if __name__ == "__main__":
    backup_recent_files()