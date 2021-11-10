from googletrans import Translator

# OUTLINE FOR CODE, THIS IS THE MOST BASIC FORM OF MY SERVICE :) !
translator = Translator()

phrase = '''yo what's up'''
result = translator.translate(phrase, dest="ja")

print(result.text)