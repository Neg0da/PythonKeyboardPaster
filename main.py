import keyboard
import pyautogui
import pyperclip
import threading
import config

print("Script started")

def debug(*args):
    """Функція для виведення повідомлення, якщо активний режим DEBUG."""
    if config.DEBUG:
        print(*args)

index = -1
debug(f"Initial index: {index}")

def load_sentences(filename="sentences.txt"):
    """Функція для завантаження речень з файлу."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            sentences = f.read().strip().split("\n")
        print(f"Loaded {len(sentences)} sentences from '{filename}'")
        return sentences
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return []
    
def paste(text: str):
    if(config.MAKE_BUFER):
        bufer = pyperclip.paste()
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "shift", "v")
    if(config.ENTER_AFTER_PASTE):
        pyautogui.press("enter")
    if(config.MAKE_BUFER):
        pyperclip.copy(bufer)

def next_sentence():
    """Переключається до наступного речення та друкує його."""
    global index
    if index < len(sentences) - 1:
        index += 1
        paste(sentences[index])
    else:
        index = 0
        debug("No more sentences. Restarting...")
        paste(sentences[index])

def previous_sentence():
    """Переключається до попереднього речення та друкує його."""
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
print("RIGHT - to type sentence")
print("LEFT - to type previous sentence")

def run_in_thread(func):
    threading.Thread(target=func, daemon=True).start()

keyboard.add_hotkey("right", lambda: run_in_thread(next_sentence))
keyboard.add_hotkey("left", lambda: run_in_thread(previous_sentence))
keyboard.wait("esc")

