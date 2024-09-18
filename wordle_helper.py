import os
import tkinter as tk
from tkinter import scrolledtext, ttk

# Load words from file
with open('5letterwords.txt') as f:
    rl = f.readlines()

# Clear the cache file at the start
with open('cache.txt', 'w', encoding='utf-8') as cache:
    cache.truncate(0)

# Function to update the cache file
def update_cache(words):
    with open('cache.txt', 'w', encoding='utf-8') as cache:
        cache.writelines(words)

# Function to read from cache file
def read_cache():
    if os.path.getsize('cache.txt') == 0:
        return []
    with open('cache.txt', 'r', encoding='utf-8') as cache:
        return cache.readlines()

# Function to handle correct letter in correct place
def correct_letter_place(letter, place):
    place = int(place) - 1
    if os.path.getsize('cache.txt') == 0:
        words = [word for word in rl if word[place] == letter]
    else:
        words = [word for word in read_cache() if word[place] == letter]
    update_cache(words)
    display_words(words)

# Function to handle wrong letters
def wrong_letters(wrong_letters):
    wrong_letters_set = set(wrong_letters)
    if os.path.getsize('cache.txt') == 0:
        words = [word for word in rl if not any(letter in word for letter in wrong_letters_set)]
    else:
        words = [word for word in read_cache() if not any(letter in word for letter in wrong_letters_set)]
    update_cache(words)
    display_words(words)

# Function to handle correct letter in wrong place
def correct_letter_wrong_place(letter, place):
    place = int(place) - 1
    if os.path.getsize('cache.txt') == 0:
        words = [word for word in rl if letter in word and word[place] != letter]
    else:
        words = [word for word in read_cache() if letter in word and word[place] != letter]
    update_cache(words)
    display_words(words)

# Function to display words in the textbox
def display_words(words):
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    for word in words:
        text_box.insert(tk.END, word)
    text_box.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Wordle Helper")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Create a style for the widgets
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Create input fields and buttons
ttk.Label(root, text="Correct Letter in Correct Place").grid(row=0, column=0, padx=10, pady=10)
letter_place_entry = ttk.Entry(root)
letter_place_entry.grid(row=0, column=1, padx=10, pady=10)
place_entry = ttk.Entry(root)
place_entry.grid(row=0, column=2, padx=10, pady=10)
ttk.Button(root, text="Submit", command=lambda: correct_letter_place(letter_place_entry.get(), place_entry.get())).grid(row=0, column=3, padx=10, pady=10)

ttk.Label(root, text="Wrong Letters").grid(row=1, column=0, padx=10, pady=10)
wrong_letters_entry = ttk.Entry(root)
wrong_letters_entry.grid(row=1, column=1, padx=10, pady=10)
ttk.Button(root, text="Submit", command=lambda: wrong_letters(wrong_letters_entry.get())).grid(row=1, column=2, padx=10, pady=10)

ttk.Label(root, text="Correct Letter in Wrong Place").grid(row=2, column=0, padx=10, pady=10)
correct_letter_entry = ttk.Entry(root)
correct_letter_entry.grid(row=2, column=1, padx=10, pady=10)
wrong_place_entry = ttk.Entry(root)
wrong_place_entry.grid(row=2, column=2, padx=10, pady=10)
ttk.Button(root, text="Submit", command=lambda: correct_letter_wrong_place(correct_letter_entry.get(), wrong_place_entry.get())).grid(row=2, column=3, padx=10, pady=10)

# Create a scrollable textbox
text_box = scrolledtext.ScrolledText(root, width=40, height=10, state=tk.DISABLED, font=("Helvetica", 12))
text_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Run the application
root.mainloop()
