# Auto Paste Script
## Description
This script automatically pastes sentences from the `sentences.txt` file using hotkeys. It supports sentence switching, clipboard usage, and different paste modes.

## Installation
### 1. Clone the repository
```
git clone <URL_REPO>
cd <PROJECT_FOLDER>
```
### 2. Install dependencies
``` 
pip install -r requirements.txt 
```
## Usage
Run the script:
```
python main.py
```
Hotkeys:

- `RIGHT` → paste the next sentence

- `LEFT` → paste the previous sentence

- `ESC` → exit the program

## Configuration File
Settings can be adjusted in `config.py`:

`DEBUG = True/False` – debug mode

`MAKE_BUFER = True/False` – save the previous clipboard buffer

`PASTE_MODE = (True, False)` – choose paste mode (`Ctrl+V` or `Ctrl+Shift+V`)

`ENTER_AFTER_PASTE = True/False` – press `Enter` after pasting

`ENTER_BEFORE_PREVIOUS = True/False` – press `Enter` before pasting the previous sentence

## `sentences.txt`

This file stores the sentences that will be pasted when using the hotkeys. Each line represents a separate sentence.