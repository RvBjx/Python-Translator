'''
This is the first version of my python translator
Its a command prompt programm without gui but it works like those versions with gui
'''
import googletrans
from googletrans import Translator, constants

translator = Translator()

print("Commands:")
print("First use lang to set languages")
print("Then use tran to translate a word or sentence")


while True:
    print(" ")
    print(" ")
    com=input("Command:")

    if(com=="lang"):
        srcme=input("Source Language:")
        destme=input("Destination Language:")
   
    elif(com=="tran"):
        tran=input("Sentence to translate:")
        translation = translator.translate(tran, src=srcme, dest=destme)
        print(" ")
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        
    elif(com=="help"):
        print("Help:")
        print("  > Use command lang to set the base language and the language you want to translate it to")
        print("  > Use command tran to translate things from base language to the other language")
        print("  > Use command exit to exit the programm")
        print("  > Use command list to see a list of available languages")
        print("-----")
        print("This translator was made by Roman Bühlmann")
        
    elif(com=="list"):
        print("List of available languages:")
        print(googletrans.LANGUAGES)
        
        
    elif(com=="exit"):
        break
    
    else:
        print("", com," is not registered")
