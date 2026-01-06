#This code copies all the files in a directory and its subdirectories into a new folder

import os
import shutil
import argparse
import re
from pathlib import Path


def _translate_windows_drive_to_wsl(path: str, require_exists: bool = False) -> str:
    """If path looks like a Windows drive (C:\\...), translate to /mnt/c/....

    If `require_exists` is True, only return the translated path when it exists on the filesystem;
    otherwise always return the translated candidate so destinations will be adjacent to original.
    """
    # Normalize backslashes
    p = path.replace('\\', '/')
    m = re.match(r'^([A-Za-z]):/(.*)', p)
    if m:
        drive = m.group(1).lower()
        rest = m.group(2)
        candidate = f"/mnt/{drive}/{rest}"
        if not require_exists:
            return candidate
        if os.path.exists(candidate):
            return candidate
    return path


def _unique_dest_path(path: str) -> str:
    """Return a non-colliding filename by appending numbered suffixes if needed."""
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 1
    while True:
        candidate = f"{base}_{i}{ext}"
        if not os.path.exists(candidate):
            return candidate
        i += 1


def copy_files_preserve_structure(src_folder: str, dest_folder: str) -> None:
    src = Path(src_folder)
    if not src.exists():
        print(f"Source folder '{src_folder}' does not exist.")
        return
    if not src.is_dir():
        print(f"Source '{src_folder}' is not a directory.")
        return

    dest_root = Path(dest_folder)
    dest_root.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(src):
        root_path = Path(root)
        rel = root_path.relative_to(src)
        target_dir = dest_root.joinpath(rel)
        target_dir.mkdir(parents=True, exist_ok=True)

        for fname in files:
            src_path = root_path.joinpath(fname)
            dest_path = target_dir.joinpath(fname)
            dest_path_str = str(dest_path)
            if os.path.exists(dest_path_str):
                dest_path_str = _unique_dest_path(dest_path_str)
            shutil.copy2(str(src_path), dest_path_str)
            print(f"Copied: {src_path} -> {dest_path_str}")


def copy_flatten(src_folder: str, dest_folder: str) -> None:
    src = Path(src_folder)
    if not src.exists() or not src.is_dir():
        print(f"Source folder '{src_folder}' does not exist or is not a directory.")
        return

    dest_root = Path(dest_folder)
    dest_root.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(src):
        root_path = Path(root)
        for fname in files:
            src_path = root_path.joinpath(fname)
            dest_path = dest_root.joinpath(fname)
            dest_path_str = str(dest_path)
            if os.path.exists(dest_path_str):
                dest_path_str = _unique_dest_path(dest_path_str)
            shutil.copy2(str(src_path), dest_path_str)
            print(f"Copied: {src_path} -> {dest_path_str}")


def main():
    parser = argparse.ArgumentParser(description='Copy all files from a directory and its subdirectories into a new folder')
    parser.add_argument('source', help='Source directory (accepts Windows C:\\... or WSL /mnt/c/...)')
    parser.add_argument('destination', nargs='?', help='Destination directory (optional, defaults to source + " ReOrganised")')
    parser.add_argument('--preserve-structure', action='store_true', help='Preserve subdirectory structure instead of flattening into a single folder')

    args = parser.parse_args()

    raw_source = args.source

    # Default destination should be adjacent to the original folder (use the original input for this)
    if args.destination:
        raw_dest = args.destination
    else:
        raw_dest = raw_source + ' ReOrganised'

    # Translate paths: for source require the translated path to exist (if running under WSL)
    source_directory = _translate_windows_drive_to_wsl(raw_source, require_exists=True)
    # For destination, translate even if the path doesn't yet exist so it's adjacent to source
    destination_directory = _translate_windows_drive_to_wsl(raw_dest, require_exists=False)

    if args.preserve_structure:
        copy_files_preserve_structure(source_directory, destination_directory)
    else:
        copy_flatten(source_directory, destination_directory)


if __name__ == '__main__':
    main()

