# FileSurfacer

A Python utility that recursively copies all files from a directory and its subdirectories into a single destination folder.

## Description

FileSurfacer flattens nested directory structures by extracting all files from a source folder and its subdirectories and placing them into a single destination folder. This is useful for:

- Collecting media files scattered across multiple folders
- Consolidating documents from complex directory hierarchies
- Preparing files for batch processing that expects a flat structure

## Installation

No external dependencies required. Just needs Python 3.

```bash
python3 FileSurfacer.py <source_directory> [destination_directory]
```

## Usage

### Basic Usage

Copy all files from a directory to a new "ReOrganised" folder:

```bash
python3 FileSurfacer.py "/path/to/source"
```

This creates a new folder named `source ReOrganised` in the same location.

### With Custom Destination

Specify a custom destination folder:

```bash
python3 FileSurfacer.py "/path/to/source" "/path/to/destination"
```

## Examples

**Example 1: Collect audiobooks**
```bash
python3 FileSurfacer.py "/home/user/Audiobooks/2024"
```
All audio files from nested folders are copied to `/home/user/Audiobooks/2024 ReOrganised`.

**Example 2: Consolidate with custom destination**
```bash
python3 FileSurfacer.py "/home/user/Documents" "/home/user/AllDocuments"
```
All files are flattened into `/home/user/AllDocuments`.

## Arguments

- `source` (required): Source directory path
- `destination` (optional): Destination directory path. If not provided, defaults to source directory + " ReOrganised"

## Notes

- Files are copied recursively from all subdirectories
- The original directory structure is not preserved
- If the destination folder doesn't exist, it will be created automatically
- Files are copied with their original metadata preserved (`shutil.copy2`)