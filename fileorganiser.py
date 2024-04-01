import os
import shutil
# os.makedirs("F:\BBA\moved")
# os.replace()
desktop="c:\\Users\\NSC\Desktop"
download="c:\\Users\\NSC\\Downloads"
paths=[desktop,download]
# Below is a simple Python program to organize files in a directory.
# This script will categorize files into subdirectories based on their file extensions.

import os
from pathlib import Path

def organize_directory(path):
    """
    Organize files in the given directory into subdirectories based on file extensions.
    
    :param path: Path to the directory to organize
    """
    # Change working directory to the given path
    os.chdir(path)
    
    # Gather all files in the directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # Loop over all files
    for file in files:
        # Get the file extension
        file_extension = Path(file).suffix.lower()
        
        # If the file has an extension, proceed to organize
        if file_extension:
            # Directory name is the file extension without the dot
            directory_name = file_extension[1:]
            
            # Create the directory if it does not exist
            os.makedirs(directory_name, exist_ok=True)
            
            # Move the file into the directory
            try:
                os.rename(file, os.path.join(directory_name, file))
            except  Exception as e:
                os.remove(file)
                print(e)
    
    print(f'Files in {path} have been organized.')

# Example usage:
# organize_directory('/path/to/directory')

# Note: This will not be executed here as we don't have permission to organize files in the environment
# and also because we don't have a sample directory to organize.
# Users should use this script on their own local machine and replace '/path/to/directory' with their directory path.
    
from shutil import move

def organize_directory_(path):
    """
    Organize files and application shortcuts in the given directory into subdirectories based on file extensions.
    
    :param path: Path to the directory to organize
    """
    # Change working directory to the given path
    os.chdir(path)
    
    # Gather all files in the directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # Define common application shortcut extensions for Windows and MacOS
    shortcut_extensions = {'.lnk', '.url', '.app', '.desktop'}
    
    # Loop over all files
    for file in files:
        # Get the file extension
        file_extension = Path(file).suffix.lower()
        
        # Check if the file is an application shortcut
        if file_extension in shortcut_extensions:
            directory_name = 'Shortcuts'
        elif file_extension:
            # Directory name is the file extension without the dot
            directory_name = file_extension[1:]
        else:
            continue  # Skip files without an extension
        
        # Create the directory if it does not exist
        if directory_name in os.listdir(path):
            pass
        else:
            os.makedirs(directory_name, exist_ok=True)
        
        # Move the file into the directory
        move(file, os.path.join(directory_name, file))
    
    print(f'Files and application shortcuts in {path} have been organized.')

# Example usage:
# Please note that this script should be run locally and with caution.
# organize_directory('/path/to/directory')

# Note: As mentioned before, this script won't be executed here because it involves file system operations.
# Please run this script on your own local machine.
    
for path in paths:
    organize_directory(path)

organize_directory("c:\\Users\\NSC\\Videos")
