import googletrans
from googletrans import Translator, constants
import time
import tkinter
from tkinter import *

translator = Translator()
isLanguageSelected=False
srcLang_entry = "0"
destLang_entry = "0"


def textToTranslateButton_action():
    srcLang_entry = clickedSource.get()
    destLang_entry = clickedDestination.get()
    translateText_entry = textToTranslateEntry.get()
    translation = translator.translate(translateText_entry, src=srcLang_entry, dest=destLang_entry)
    endTextLabel.config(text=f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


window = Tk()
window.title("Translator V3")
window.geometry("300x200")

optionsSource = [
    'af','afrikaans','sq','albanian','am','amharic','ar','arabic','hy','armenian','az','azerbaijani','eu','basque','be','belarusian','bn','bengali','bs','bosnian','bg','bulgarian','ca','catalan','ceb','cebuano','ny','chichewa','zh-cn','chinese(simplified)','zh-tw','chinese(traditional)','coi','corsican','hr','croatian','cs','czech','da','danish','nl','dutch','en','english','eo','esperanto','et','estonian','tl','filipino','fi','finnish','fr','french','fy','frisian','gl','galician','ka','georgian','de','german','el','greek','gu','gujarati','ht','haitiancreole','ha','hausa','haw','hawaiian','iw','hebrew','he','hebrew','hi','hindi','hmn','hmong','hu','hungarian','is','icelandic','ig','igbo','id','indonesian','ga','irish','it','italian','ja','japanese','jw','javanese','kn','kannada','kk','kazakh','km','khmer','ko','korean','ku','kurdish','ky','kyrgyz','lo','lao','la','latin','lv','latvian','lt','lithuanian','lb','luxembourgish','mk','macedonian''mg','malagasy','ms','malay','ml','malayalam','mt','maltese','mi','maori','mr','marathi','mn','mongolian','my','myanmar(burmese)','ne','nepali','no','norwegian','or','odia','ps','pashto','fa','persian','pl','polish','pt','portuguese','pa','punjabi','ro','romanian','ru','russian','sm','samoan','gd','scotsgaelic','sr','serbian','st','sesotho','sn','shona','sd','sindhi','si','sinhala','sk','slovak','sl','slovenian','so','somali','es','spanish','su','sundanese','sw','swahili','sv','swedish','tg','tajik','ta','tamil','te','telugu','th','thai','tr','turkish','uk','ukrainian','ur','urdu','ug','uyghur','uz','uzbek','vi','vietnamese','cy','welsh','xh','xhosa','yi','yiddish','yo','yoruba','zu','zulu',]
optionsDestination = [
    'af','afrikaans','sq','albanian','am','amharic','ar','arabic','hy','armenian','az','azerbaijani','eu','basque','be','belarusian','bn','bengali','bs','bosnian','bg','bulgarian','ca','catalan','ceb','cebuano','ny','chichewa','zh-cn','chinese(simplified)','zh-tw','chinese(traditional)','coi','corsican','hr','croatian','cs','czech','da','danish','nl','dutch','en','english','eo','esperanto','et','estonian','tl','filipino','fi','finnish','fr','french','fy','frisian','gl','galician','ka','georgian','de','german','el','greek','gu','gujarati','ht','haitiancreole','ha','hausa','haw','hawaiian','iw','hebrew','he','hebrew','hi','hindi','hmn','hmong','hu','hungarian','is','icelandic','ig','igbo','id','indonesian','ga','irish','it','italian','ja','japanese','jw','javanese','kn','kannada','kk','kazakh','km','khmer','ko','korean','ku','kurdish','ky','kyrgyz','lo','lao','la','latin','lv','latvian','lt','lithuanian','lb','luxembourgish','mk','macedonian''mg','malagasy','ms','malay','ml','malayalam','mt','maltese','mi','maori','mr','marathi','mn','mongolian','my','myanmar(burmese)','ne','nepali','no','norwegian','or','odia','ps','pashto','fa','persian','pl','polish','pt','portuguese','pa','punjabi','ro','romanian','ru','russian','sm','samoan','gd','scotsgaelic','sr','serbian','st','sesotho','sn','shona','sd','sindhi','si','sinhala','sk','slovak','sl','slovenian','so','somali','es','spanish','su','sundanese','sw','swahili','sv','swedish','tg','tajik','ta','tamil','te','telugu','th','thai','tr','turkish','uk','ukrainian','ur','urdu','ug','uyghur','uz','uzbek','vi','vietnamese','cy','welsh','xh','xhosa','yi','yiddish','yo','yoruba','zu','zulu',]

textToTranslateButton = Button(window, text="Set txt", command=textToTranslateButton_action)

textToTranslateEntry = Entry(window, bd=5, width=20)

endTextLabel = Label(window)

clickedSource = StringVar()
clickedSource.set("Source")
clickedDestination = StringVar()
clickedDestination.set("Destination")

dropSource = OptionMenu(window, clickedSource, *optionsSource)
dropDestination = OptionMenu(window, clickedDestination, *optionsDestination)

dropSource.grid(row=0, column=0, pady = 10)
dropDestination.grid(row=0, column=1, pady = 10)

textToTranslateButton.grid(row=2, column=1, pady = 10)
textToTranslateEntry.grid(row=2, column=0, pady = 10)

endTextLabel.grid(row = 3, column = 0, columnspan = 2)

window.mainloop()