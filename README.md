# Python_Modules

# 1. File Organization and Auto-Renaming using Watchdog

This Python script uses the Watchdog library to monitor a specified directory (`from_dir`) for newly created files. When a new file is created, the program automatically moves it to a categorized destination directory (`to_dir`). If a file with the same name already exists in the target directory, the file is renamed with a random number to prevent overwriting.

## Features

- **Automated File Movement**: Monitors a source directory for new files and moves them to categorized subdirectories within the destination directory.
- **Auto-Renaming**: If a file with the same name exists, the script appends a random number to the filename.
- **File Organization by Type**: Organizes files based on their extensions (e.g., images, videos, documents).

## Requirements

- **Watchdog Library**: Install Watchdog with the following command:
  ```bash
  pip install watchdog
  ```

## File Structure

The script organizes files into these categories:
- **Image_files**: `.jpg`, `.jpeg`, `.png`
- **Video_files**: `.mp4`, `.mp3`, `.mov`
- **Document_files**: `.ppt`, `.csv`, `.pdf`

## Configuration

1. Set your source (`from_dir`) and destination (`to_dir`) directories:
   ```python
   from_dir = "c:/Users/HP EliteBook 840 G4/Downloads"
   to_dir = "C:/Users/HP EliteBook 840 G4/BlockVerse Assignments/PYTEST"
   ```

2. Customize file categories and extensions in the `dir_tree` dictionary as needed.

## How It Works

1. **Initialize Watchdog Observer**: The observer monitors the `from_dir` for file creation events.
2. **Event Handling**:
   - When a new file is created, the `on_created` event triggers.
   - The program checks the file extension to determine its category.
   - If a file with the same name already exists in the target directory, a random 4-digit number is appended to the filename.
3. **File Moving and Organizing**:
   - Files are moved to the appropriate folder in `to_dir`.
   - If the category folder doesn’t exist, it is created automatically.

## Usage

1. **Run the Script**: Start the script by executing:
   ```bash
   python watchdog_script.py
   ```

2. **File Monitoring**: The program will monitor the `from_dir` directory for new files. Any files added will be organized and moved to `to_dir`.

3. **Stopping the Script**: Press `CTRL+C` to stop the observer.

## Code Overview

- **FileMovementHandler Class**:
  - Contains the `on_created` method to handle file creation events.
  - Moves files to categorized folders, and appends a random number to the filename if necessary.
  
- **Observer Setup**:
  - An observer is set up to monitor the `from_dir` directory and is started in a loop.

## Example Output

When a file is moved:
```
Downloaded file.jpg
Directory exists...
File with the same name exists, renaming to file_1234.jpg
Moving file.jpg ...
```

## Notes

- **Recursive Monitoring**: The script includes `recursive=True`, so it also monitors subdirectories within `from_dir`.
- **Cross-Platform Paths**: Adjust the `from_dir` and `to_dir` paths if running on a different operating system.


This script is an efficient solution for automated file organization and renaming, especially useful for monitoring download folders or other file-heavy directories.
____________________________________________________________________________________________________________________________________________________________________
