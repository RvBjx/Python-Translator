import googletrans
from googletrans import Translator, constants
import time

translator = Translator()

isLanguageSelected=False

needHelp=input("Do you need help? Y/n ").upper()

if(needHelp=="Y"):
    print("List of available languages:")
    print(googletrans.LANGUAGES)
 
# while-Loop
while True:
    if(not isLanguageSelected):
        print("")
        print("Set languages:")
        
    
        sourceLanguage=input("Source Language: ")
        destinationLanguage=input("Destination Language: ")
        
        isLanguageSelected=True
    
    textToTranslate=input("Sentence to translate: ")
    translation = translator.translate(textToTranslate, src=sourceLanguage, dest=destinationLanguage)
    print("")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    print("")
    
    end=input("Exit? Y/ ").upper()
    if(end=="Y"):
        print('\n' * 2)
        print("Goodbye...")
        time.sleep(1)
        break
    
        
    
    changeLanguage=input("Change language? Y/n ").upper()
    if(changeLanguage=="Y"):
        isLanguageSelected="0"
        print("")