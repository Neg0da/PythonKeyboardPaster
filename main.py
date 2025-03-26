import keyboard
import pyautogui
import time

print("Script started")

# Читаємо файл як список рядків
with open("sentences.txt", "r", encoding="utf-8") as f:
    sentences = f.read().strip().split("\n")

index = -1

def type_sentence():
    """Вводить поточне речення у активне вікно."""
    global index
    time.sleep(0.1)
    pyautogui.write(sentences[index], interval=0.05)
    pyautogui.press("enter")

def next_sentence():
    """Переключається до наступного речення та друкує його."""
    global index
    if index < len(sentences) - 1:  # Не виходимо за межі списку
        index += 1
        type_sentence()

def prev_sentence():
    """Переключається до попереднього речення та друкує його."""
    global index
    if index > 0:  # Не виходимо за межі списку
        index -= 1
        type_sentence()

print("The program is running in the background.")
print("Hotkeys:")
print("- End → type the next sentence")
print("- Home → go back to the previous sentence")
print("- Esc → exit")

keyboard.add_hotkey("End", next_sentence)  # Натискання End друкує наступне речення
keyboard.add_hotkey("Home", prev_sentence)  # Натискання Home друкує попереднє речення
keyboard.wait("esc")  # Чекаємо натискання Escape для виходу
