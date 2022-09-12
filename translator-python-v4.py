'''
This version of my translator was made using a tutorial for the list comprehension and textblob things and for the comboboxes.
Build a Language Translator App - Python Tkinter GUI Tutorial 200
from Codemy.com on YouTube
'''
import googletrans
from googletrans import Translator, constants
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import textblob

translator = Translator()

# define translation process
def translate():
    translated_text.config(state="normal")
    translated_text.delete(1.0, END)
    try:
        for key, value in languages.items():
            if (value == source_combo.get()):
                from_language_key = key
        
        for key, value in languages.items():
            if (value == destination_combo.get()):
                to_language_key = key
        words = textblob.TextBlob(original_text.get(1.0, END))
        
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        
        translated_text.insert(1.0, words)
        translated_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Translator", e)
# define clear button function
def clear():
    translated_text.config(state="normal")
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)
    translated_text.config(state="disabled")

# diefine the name of the tkinter window and title
window = Tk()
window.title("Translator V4")

# Get language list from googletrans
languages = googletrans.LANGUAGES
# Convert language list from googletrans to python list
language_list = list(languages.values())


# define all gui elements
original_text = Text(window, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translated_text = Text(window, height=10, width=40, state="disabled")
translated_text.grid(row=0, column=2, pady=20, padx=10)

translate_button = Button(window, text="Translate", font=("Helvetica", 24), command = translate)
translate_button.grid(row=0, column=1, padx=10)

source_combo = ttk.Combobox(window, width=20, value=language_list)
source_combo.current(21)
source_combo.grid(row=2, column=0, )

destination_combo = ttk.Combobox(window, width=20, value=language_list)
destination_combo.current(26)
destination_combo.grid(row=2, column=2, )

clear_button = Button(window, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

window.mainloop()