import os
import shutil

def copy_static_files(working_directory, log=False):
    WORKING_DIR = os.path.abspath(working_directory)
    DESTINATION_DIR = os.path.normpath(os.path.join(WORKING_DIR, "public"))
    os.makedirs(DESTINATION_DIR, exist_ok=True)
    SOURCE_DIR = os.path.normpath(os.path.join(WORKING_DIR, "static"))
    delete_files_in_directory(DESTINATION_DIR, log=log)
    copy_files_in_directory(SOURCE_DIR, DESTINATION_DIR, log=log)
    

def delete_files_in_directory(directory, log=False):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            if log:
                print(f"Deleting file: {file_path}")
            os.remove(file_path)
        elif os.path.isdir(file_path):
            delete_files_in_directory(file_path, log=log)
            if log:
                print(f"Deleting directory: {file_path}")
            os.rmdir(file_path)

def copy_files_in_directory(source_dir, destination_dir, log=False):
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)
        if os.path.isfile(source_item):
            if log:
                print(f"Copying file from {source_item} to {destination_item}")
            shutil.copy2(source_item, destination_item)
        elif os.path.isdir(source_item):
            if log:
                print(f"Creating directory: {destination_item}")
            os.makedirs(destination_item, exist_ok=True)
            copy_files_in_directory(source_item, destination_item, log=log)