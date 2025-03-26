import keyboard
import pyautogui
import time
import threading

print("Script started")

# Читаємо файл як список рядків
try:
    with open("sentences.txt", "r", encoding="utf-8") as f:
        sentences = f.read().strip().split("\n")
    print(f"Loaded {len(sentences)} sentences from 'sentences.txt'")
except FileNotFoundError:
    print("Error: The file 'sentences.txt' was not found. Please make sure it exists in the script's directory.")
    sentences = []

index = -1  # Ініціалізація перед першим реченням
print(f"Initial index: {index}")

def type_sentence():
    """Друкує речення символ за символом."""
    global index
    print(f"Typing sentence at index: {index}")

    if 0 <= index < len(sentences):
        sentence = sentences[index]
        print(f"Sentence to type: {sentence}")
        pyautogui.typewrite(sentence, interval=0.05)  # Повільний друк для надійності
    else:
        print("Index out of range or invalid.")

    pyautogui.press("enter")

def next_sentence():
    """Переключається до наступного речення та друкує його."""
    global index
    if index < len(sentences) - 1:
        index += 1
        type_sentence()
    else:
        print("No more sentences.")

def prev_sentence():
    """Переключається до попереднього речення та друкує його."""
    global index
    if index > 0:
        index -= 1
        type_sentence()
    else:
        print("Already at the beginning.")

def wait_for_exit():
    keyboard.wait("esc")
    print("Exiting...")
    exit()

exit_thread = threading.Thread(target=wait_for_exit, daemon=True)
exit_thread.start()

print("Hotkeys: End → next | Home → previous | Esc → exit")

keyboard.add_hotkey("End", lambda: next_sentence() if index != -1 else next_sentence())
keyboard.add_hotkey("Home", prev_sentence)
keyboard.wait("esc")
