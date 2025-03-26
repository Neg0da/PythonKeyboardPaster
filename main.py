import keyboard
import pyautogui
import pyperclip
import time

print("Script started")

# Читаємо файл як список рядків
with open("sentences.txt", "r", encoding="utf-8") as f:
    sentences = f.read().strip().split("\n")

index = -1  # Ініціалізація перед першим реченням

def type_sentence():
    """Копіює поточне речення в буфер обміну та вставляє його через Ctrl + V."""
    global index
    time.sleep(0.1)
    
    # Копіюємо поточне речення в буфер обміну
    pyperclip.copy(sentences[index])
    
    # Вставляємо через Ctrl + V
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

def next_sentence():
    """Переключається до наступного речення та вставляє його."""
    global index
    if index < len(sentences) - 1:
        index += 1  # Збільшуємо індекс після того, як вже вставили
        type_sentence()

def prev_sentence():
    """Переключається до попереднього речення та вставляє його."""
    global index
    if index > 0:
        index -= 1
        type_sentence()

print("The program is running in the background.")
print("Hotkeys:")
print("- End → type the next sentence")
print("- Home → go back to the previous sentence")
print("- Esc → exit")

# Використовуємо клавіші для керування
keyboard.add_hotkey("End", lambda: next_sentence() if index != -1 else next_sentence())  # Перше натискання надрукує "Sentense 1"
keyboard.add_hotkey("Home", prev_sentence)  # Натискання Home друкує попереднє речення
keyboard.wait("esc")  # Чекаємо натискання Escape для виходу
