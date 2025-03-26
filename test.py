import keyboard
import config

print("Script started")

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

def print_sentences_if_debug(sentences):
    """Функція для виведення списку речень, якщо активний режим DEBUG."""
    if config.DEBUG:
        print(sentences)

print_sentences_if_debug(load_sentences())

print("ESC - to exit")
keyboard.wait("esc")
