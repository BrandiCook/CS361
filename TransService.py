from googletrans import Translator
from time import sleep

# *** PLEASE NOTE THE BELOW INFORMATION ON HOW TO INSTALL ***
# "pip install googletrans==3.1.0a0" is required before running this service

# All you, as the user of this service, need to do is change the text in "request.txt" to whatever you want! :D
# If you dont want it to print to the console, you can remove the print(text_to_translate) and
# print(translated_text.text)


# I used official information from the makers of google trans at https://py-googletrans.readthedocs.io/en/latest/

""" 
# OUTLINE FOR CODE, THIS IS THE MOST BASIC FORM OF MY SERVICE :) !
translator = Translator()

phrase = '''yo what's up'''
result = translator.translate(phrase, dest="ja")

print(result.text)
"""

request_file = "request.txt"
response_file = "response.txt"


while True:
    # opens the txt file
    f = open("request.txt", 'r')
    a = open("response.txt", 'a')
    if f.mode == 'r':
        text_to_translate = f.read()
        # Prints the text that will eventually be translated
        print(text_to_translate)

    translator = Translator()

    # translate contents of request.txt
    translated_text = translator.translate(text_to_translate, dest="es")
    # Prints the translated text
    print(translated_text.text)

    # More supported languages can be found at https://py-googletrans.readthedocs.io/en/latest/, just scroll down!

    # write translation to the response.txt
    # I had to add encoding = utf-8 for it to work with certain languages, like Japanese for example
    with open('response.txt', 'w', encoding="utf-8") as f:
        f.write(translated_text.text)

    f.close()
    a.close()

    sleep(20)

