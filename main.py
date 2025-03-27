#main.py

import keyboard
import pyautogui
import pyperclip
import threading
import config

print("Script started")

def debug(*args):
    """If DEBUG is enabled - print it in console."""
    if config.DEBUG:
        print(*args)

index = -1
debug(f"Initial index: {index}")

def load_sentences(filename="sentences.txt"):
    """Loading sentences from file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            sentences = f.read().strip().split("\n")
        debug(f"Loaded {len(sentences)} sentences from '{filename}'")
        return sentences
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return []
    
paste_index = 0

def paste(text: str):
    """Paste sentence."""
    if(config.MAKE_BUFER):
        bufer = pyperclip.paste()
    pyperclip.copy(text)
    if config.PASTE_MODE[0]:
        pyautogui.hotkey("ctrl", "v")
    elif config.PASTE_MODE[1]:
        pyautogui.hotkey("ctrl", "shift", "v")
    else:
        debug(f"Unknown PASTE_MODE: {config.PASTE_MODE}")
    if(config.ENTER_AFTER_PASTE):
        pyautogui.press("enter")
    if(config.MAKE_BUFER):
        pyperclip.copy(bufer)

def next_sentence():
    """Switch to next sentence and paste it."""
    global index
    if index < len(sentences) - 1:
        index += 1
        paste(sentences[index])
    else:
        index = 0
        debug("No more sentences. Restarting...")
        paste(sentences[index])

def previous_sentence():
    """Switch to previous sentence and paste it."""
    global index
    if index > 0:
        index -= 1
        if(config.ENTER_BEFORE_PREVIOUS):
            pyautogui.press("enter")
        paste(sentences[index])
    else:
        index = 0
        debug("It's the first sentence. Can't go back.")
        if(config.ENTER_BEFORE_PREVIOUS):
            pyautogui.press("enter")
        paste(sentences[index])

sentences = load_sentences()
debug(sentences)

print("ESC - to exit")
print("RIGHT - to paste sentence")
print("LEFT - to paste previous sentence")

def run_in_thread(func):
    threading.Thread(target=func, daemon=True).start()

keyboard.add_hotkey("right", lambda: run_in_thread(next_sentence))
keyboard.add_hotkey("left", lambda: run_in_thread(previous_sentence))
keyboard.wait("esc")