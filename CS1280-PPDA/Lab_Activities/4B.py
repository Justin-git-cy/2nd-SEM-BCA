import shutil
import os

def file_operations(source, destination, operation):
    """Performs renaming, copying, and moving of files."""
    if operation == 'rename':
        os.rename(source, destination)
    elif operation == 'copy':
        shutil.copy(source, destination)
    elif operation == 'move':
        shutil.move(source, destination)
