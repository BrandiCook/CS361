from googletrans import Translator

# *** PLEASE NOTE THE BELOW INFORMATION ON HOW TO INSTALL ***
# "pip install googletrans==3.1.0a0" is required before running this service

# All you, as the user of this service, need to do is change the text in "request.txt" to whatever you want! :D


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

# opens the txt file
f = open("request.txt", 'r')
a = open("response.txt", 'a')
if f.mode == 'r':
    text_to_translate = f.read()
    print(text_to_translate)

translator = Translator()

# translate contents of request.txt
translated_text = translator.translate(text_to_translate, dest="es")
print(translated_text.text)

# write translation to the response.txt
with open('response.txt', 'w') as f:
    f.write(translated_text.text)
