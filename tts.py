try:
  from PIL import Image
except ImportError:
  import Image
import pytesseract

def ocr_core(filename):
  text=pytesseract.image_to_string(Image.open(filename))
  return text

mytext=ocr_core('image.jpg')
print(mytext)


from gtts import gTTS
import os
tts = gTTS(text=mytext, lang='en')
tts.save("mytext.mp3")
os.system("mpg321 mytext.mp3")
