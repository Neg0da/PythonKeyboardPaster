import keyboard
import pyautogui
import pyperclip
import time

print("Script started")

# Читаємо файл як список рядків
try:
    with open("sentences.txt", "r", encoding="utf-8") as f:
        sentences = f.read().strip().split("\n")
except FileNotFoundError:
    print("Error: The file 'sentences.txt' was not found. Please make sure it exists in the script's directory.")
    sentences = []

index = -1  # Ініціалізація перед першим реченням

def type_sentence():
    """Копіює поточне речення в буфер обміну та вставляє його через Ctrl + V."""
    if 0 <= index < len(sentences):
        pyperclip.copy(sentences[index])
    else:
        keyboard.write(pyperclip.paste())
        time.sleep(0.1)
    
    # Копіюємо поточне речення в буфер обміну
    pyperclip.copy(sentences[index])
    
    # Вставляємо через Ctrl + V
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

def next_sentence():
    """Переключається до наступного речення та вставляє його."""
    global index
    if index > 0:
        index -= 1
        type_sentence()
    elif index == -1:
        print("The program is actively waiting for hotkey inputs.")

def prev_sentence():
    """Переключається до попереднього речення та вставляє його."""
    global index
    if index > 0:
        index -= 1
keyboard.add_hotkey("End", next_sentence)  # Перше натискання надрукує "Sentense 1"

import threading

def wait_for_exit():
    keyboard.wait("esc")  # Чекаємо натискання Escape для виходу
    print("Exiting program...")
    exit()

# Запускаємо очікування натискання Escape в окремому потоці
exit_thread = threading.Thread(target=wait_for_exit, daemon=True)
exit_thread.start()
print("Hotkeys:")
print("- End → type the next sentence")
print("- Home → go back to the previous sentence")
print("- Esc → exit")

# Використовуємо клавіші для керування
keyboard.add_hotkey("End", lambda: next_sentence() if index != -1 else next_sentence())  # Перше натискання надрукує "Sentense 1"
keyboard.add_hotkey("Home", prev_sentence)  # Натискання Home друкує попереднє речення
keyboard.wait("esc")  # Чекаємо натискання Escape для виходу
