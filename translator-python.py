'''
Note:

programm file is a .pyw to open it without visible command prompt if opened through python as an app from the microsoft store
important comments/descriptions are in green (made with quotation marks) and smaller comments are made with hashtag
the front end of our programm is mostly held in german, although there might be english words in the export files since the language list from the googletrans library is in english
'''

'importing all the necessary librarys'
import googletrans
from googletrans import Translator
from tkinter import *
from tkinter import ttk, messagebox
import textblob
from gtts import gTTS
import pygame
import os
import time

'starting the timer'
start = time. time()
end = ""

'creating variables for later'
words = ""
to_language_key = ""
basewords = ""
from_language_key = ""

'defining translation process'
def translate():
    #sets text box "translated_text" to state normal to be able to write inside it
    translated_text.config(state="normal")
    #deletes all content in "translated_text"
    translated_text.delete(1.0, END)
    #reading from_language and to_language as keys from combo box
    try:
        for key, value in languages.items():
            if (value == source_combo.get()):
                from_language_key = key
        
        for key, value in languages.items():
            if (value == destination_combo.get()):
                global to_language_key
                to_language_key = key
        global words
        global basewords
        #using textblob library to get content from text field "original_text"
        basewords = textblob.TextBlob(original_text.get(1.0, END))
        #translating the contents of "original_text" to destination language with googletrans library
        words = basewords.translate(from_lang=from_language_key, to=to_language_key)
        #inserting results into "translated_text" text field
        translated_text.insert(1.0, words)
        # changing state of "translated_text" to disable for user to not be able to write inside
        translated_text.config(state="disabled")
    #would show a messagebox if an error would occur
    except Exception as e:
        messagebox.showerror("Übersetzer", e)
        
'defines listen action -> text to speech with gTTS and pygame'  
def listen():
    # converting content of variables to string for programm to understand
    text = str(words)
    # text to speech with gTTS
    tts = gTTS(text, lang=str(to_language_key), lang_check=True,)
    #defining name of audio output file and saving text to speech there
    filename = "audio.mp3"
    tts.save(filename)
    # plays the mp3 file with pygame
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()
    # waiting on pygame to finish playing mp3 file, then deleting it
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)
    else:
        pygame.mixer.music.unload()
    os.remove("audio.mp3")
    
'defines clear button action -> clearing both text fields'
def clear():
    translated_text.config(state="normal")
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)
    translated_text.config(state="disabled")

'defines action that happens on closing the programm -> timer'
def on_closing():
    # ending timer
    end = time.time()
    # converting timer results to more readeable result
    end_time = int(end - start)
    # creating messagebox for output
    if messagebox.showinfo("Übersetzer", f"Du hast den Übersetzer {end_time} Sekunden gebraucht."):
        window.destroy()
        
'defines action for pressing the menu selection export'
def export():
    # unique name for export file
    exportnumber = time.time()
    # get values from combo boxes
    for key, value in languages.items():
        if (value == source_combo.get()):
            exportlang_1 = value
    for key, value in languages.items():
        if (value == destination_combo.get()):
            exportlang_2 = value
    # creates the file with a unique name and fills in the content
    exportfile = open(f"export-{exportnumber}.txt", "w")
    content = [f"Eingabe-Sprache: {exportlang_1}\n", f"Eingabe: {basewords}\n","", f"Übersetzt zu: {exportlang_2}\n", f"Ergebniss: {words}\n"]
    exportfile.writelines(content)
    exportfile.close()

'defines tkinter window and title'
window = Tk()
window.title("Übersetzer")
window.geometry("870x250")

'importing list of languages from googletrans library'
languages = googletrans.LANGUAGES
# Convert language list from googletrans to python list
language_list = list(languages.values())


'defining all tkinter gui elements '
# menu bar
menu = Menu(window)
window.config(menu=menu)
settingsmenu = Menu(menu)
menu.add_cascade(label="Mehr", menu=settingsmenu)
settingsmenu.add_command(label="Exportieren", command=export)
# first text field
original_text = Text(window, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)
# second text field
translated_text = Text(window, height=10, width=40, state="disabled")
translated_text.grid(row=0, column=2, pady=20, padx=10)
# button to trigger translate function
translate_button = Button(window, text="Übersetzen", font=("Helvetica", 24), command = translate)
translate_button.grid(row=0, column=1, padx=10)
# button to trigger listen function
listen_button = Button(window, text="Anhören", command = listen, )
listen_button.grid(row=2, column=1,sticky='E')
# source combo for languages to choose from
source_combo = ttk.Combobox(window, width=20, value=language_list)
source_combo.current(21)
source_combo.grid(row=2, column=0, )
# destination combo for languages to choose from
destination_combo = ttk.Combobox(window, width=20, value=language_list)
destination_combo.current(26)
destination_combo.grid(row=2, column=2, )
# button to trigger clear funtion
clear_button = Button(window, text="Löschen", command=clear)
clear_button.grid(row=2, column=1,sticky='W')

'calling on_closing function when closing programm'
window.protocol("WM_DELETE_WINDOW", on_closing)

'closing of our little programm with this line.'
window.mainloop()