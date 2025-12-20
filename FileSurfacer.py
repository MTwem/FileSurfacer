#This code copies all the files in a directory and its subdirectories into a new folder

import os
import shutil
import argparse

def copy_files(src_folder, dest_folder):
    # Check if source folder exists
    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist.")
        return

    # Check if destination folder exists, create if not
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate over files in the source folder
    for filename in os.listdir(src_folder):
        src_path = os.path.join(src_folder, filename)
        if os.path.isdir(src_path):
            copy_files(src_path, dest_folder)
        else:
            dest_path = os.path.join(dest_folder, filename)

            # Copy the file to the destination folder
            shutil.copy2(src_path, dest_path)
            print(f"File '{filename}' copied to '{dest_folder}'.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy all files from a directory and its subdirectories into a new folder')
    parser.add_argument('source', help='Source directory')
    parser.add_argument('destination', nargs='?', help='Destination directory (optional, defaults to source + " ReOrganised")')
    
    args = parser.parse_args()
    
    source_directory = args.source
    destination_directory = args.destination if args.destination else source_directory + ' ReOrganised'
    
    copy_files(source_directory, destination_directory)

