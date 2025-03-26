import keyboard
import pyautogui
import time
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

def type_sentence():
    """Друкує речення символ за символом."""
    global index
    index += 1
    debug(f"Typing sentence at index: {index}")

    if index < len(sentences):
        sentence = sentences[index]
        debug(f"Sentence to type: {sentence}")
        pyautogui.typewrite(sentence, interval=0.05)
        debug("Sentence typed")
    else:
        debug("Index out of range or invalid.")

    pyautogui.press("enter")
    debug("Enter pressed")

def next_sentence():
    """Переключається до наступного речення та друкує його."""
    global index
    if index < len(sentences):
        index += 1
        type_sentence()
    else:
        index = -1
        debug("No more sentences. Restarting...")

sentences = load_sentences()
debug(sentences)

print("ESC - to exit")
print("RIGHT - to type sentence")

keyboard.add_hotkey("right", lambda: threading.Thread(target=next_sentence).start())
keyboard.wait("esc")

