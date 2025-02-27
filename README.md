# goit-pythonweb-hw-04

Homework 4. Fullstack Web Development with Python at GoIT Neoversity

# Asynchronous File Sorter

This Python script asynchronously reads files from the specified source directory and sorts them into subdirectories in the target directory based on file extensions. The script utilizes asynchronous programming for efficient processing of a large number of files.

## Features
- Recursively reads files from the source directory.
- Copies files to the target directory, sorting them into subdirectories based on their extensions.
- Uses asynchronous file operations for improved performance.
- Handles missing directories by creating them automatically.
- Logs errors and operations for better debugging.

## Requirements
- Python 3.7 or higher
- `aiofiles` package for asynchronous file handling

## Installation
To install dependencies, run:

```bash
pip install -r requirements.txt
```
## Usage

To execute the script, use the following command:

```bash
python script.py <source_directory> [<destination_directory>]
```
- <source_directory>: The directory containing the files to be sorted.
- <destination_directory> (optional): The directory where files will be copied and sorted. If not provided, defaults to `dist`.

## Example
Sort files from /home/user/downloads into /home/user/sorted_files:
```bash
python script.py /home/user/downloads /home/user/sorted_files
```

Sort files from /home/user/downloads into the default dist directory:
```bash
python script.py /home/user/downloads
```

## Logging

The script provides informative logs during execution. Errors and copied file details are displayed in the terminal.

## Notes
- The script uses asynchronous operations to improve performance when processing large numbers of files.
- If a file does not have an extension, it is placed in a no_extension folder.
- The script automatically creates missing destination directories.

---
