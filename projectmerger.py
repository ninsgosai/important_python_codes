import os
import shutil

def copy_files_and_folders(source_path, destination_path, skip_extensions, skip_folders):
    """
    Copies files and folders from the source path to the destination path,
    skipping files with the specified extensions, folders, and Git-related files.
    
    Args:
        source_path (str): The path to the source directory.
        destination_path (str): The path to the destination directory.
        skip_extensions (list): A list of file extensions to skip.
        skip_folders (list): A list of folder names to skip.
    """
    git_folders = ['.git']  # List of Git-related folders to skip
    docker_files = ['Dockerfile','firebase.py']  # List of Docker-related files to skip
    
    for root, dirs, files in os.walk(source_path):
        # Skip specified folders, Git-related folders, and Docker-related files
        dirs[:] = [d for d in dirs if d not in skip_folders and d not in git_folders]
        files = [f for f in files if f not in docker_files]
        
        for file in files:
            # Check if the file extension is in the skip list
            if any(file.endswith(ext) for ext in skip_extensions):
                continue
            
            # Construct the source and destination paths
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(root, source_path)
            destination_dir = os.path.join(destination_path, relative_path)
            destination_file = os.path.join(destination_dir, file)
            
            # Create the destination directory if it doesn't exist
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            
            # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")

# Example usage
source_path = ""
destination_path = ""
skip_extensions = [".pyc", ".log"]
skip_folders = ["migrations", "env", "venv"]

copy_files_and_folders(source_path,destination_path , skip_extensions, skip_folders)
