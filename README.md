# FileSurfacer

A small Python utility that gathers all files under a source directory (recursively) and copies them into a single destination folder by default.

## Key behavior

- By default the tool *flattens* all files into one folder named "<source> ReOrganised" placed adjacent to the source input.
- Use `--preserve-structure` to preserve subdirectory layout under the destination.
- When a filename collision occurs in the destination, the script appends a numeric suffix (e.g. `_1`) to avoid overwriting.
- The script accepts Windows-style paths (e.g. `C:\Users\...`) and will translate them to WSL `/mnt/c/...` when appropriate.

## Requirements

- Python 3 (no third-party packages required)

## Usage

Basic (flatten into `<source> ReOrganised`):
```bash
python3 FileSurfacer.py "/path/to/source"
```

Preserve the source directory structure under the destination:
```bash
python3 FileSurfacer.py "/path/to/source" "/path/to/destination" --preserve-structure
```

Windows / WSL examples

- Run from native Windows PowerShell (use `python` or `py`):
```powershell
python "C:\path\to\FileSurfacer.py" "C:\Users\<USER>\Desktop\ExampleFolder"
```

- Run from WSL (the script will translate `C:\...` to `/mnt/c/...` when available):
```bash
python3 /home/<USER>/FileSurfacer/FileSurfacer.py "C:\Users\<USER>\Desktop\ExampleFolder"
```

## Options

- `--preserve-structure`: keep the source directory layout inside the destination instead of flattening.

## Notes

- By default the destination is computed from the raw source input as `<source> ReOrganised` adjacent to the original folder (so it won't create a `C:\...` folder inside your Linux home).
- If you prefer skipping duplicate files instead of renaming, or want a `--dry-run` flag to preview actions, open an issue or request the change.

## Example

Flatten a Desktop folder into a single collection (WSL or Windows):
```bash
python3 FileSurfacer.py "C:\Users\<USER>\Desktop\ExampleFolder"
```

This will create `C:\Users\<USER>\Desktop\ExampleFolder ReOrganised` (or the WSL-translated equivalent) and copy all files into it.