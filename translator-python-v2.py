import googletrans
from googletrans import Translator, constants
import time
import tkinter
from tkinter import *

translator = Translator()
isLanguageSelected=False

srcLang_entry = "0"
destLang_entry = "0"

def sourceLanguageButton_action():
    global srcLang_entry
    srcLang_entry = sourceLanguageEntry.get()
    
def destinationLanguageButton_action():
    global destLang_entry
    destLang_entry = destinationLanguageEntry.get()
    
def textToTranslateButton_action():
    translateText_entry = textToTranslateEntry.get()
    translation = translator.translate(translateText_entry, src=srcLang_entry, dest=destLang_entry)
    endTextLabel.config(text=f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

fenster = Tk()
fenster.title("Translator V2")

sourceLanguageButton = Button(fenster, text="Set src", command=sourceLanguageButton_action)

sourceLanguageEntry = Entry(fenster, bd=5, width=5)

destinationLanguageButton = Button(fenster, text="Set dest", command=destinationLanguageButton_action)

destinationLanguageEntry = Entry(fenster, bd=5, width=5)

textToTranslateButton = Button(fenster, text="Set txt", command=textToTranslateButton_action)

textToTranslateEntry = Entry(fenster, bd=5, width=20)

endTextLabel = Label(fenster)


sourceLanguageButton.grid(row=0, column=1, pady = 10)
sourceLanguageEntry.grid(row=0, column=0, pady = 10)
destinationLanguageButton.grid(row=1, column=1, pady = 10)
destinationLanguageEntry.grid(row=1, column=0, pady = 10)
textToTranslateButton.grid(row=2, column=1, pady = 10)
textToTranslateEntry.grid(row=2, column=0, pady = 10)

endTextLabel.grid(row = 3, column = 0, columnspan = 2)

fenster.mainloop()