from gtts import gTTS
from langdetect import detect
import base64


def audio(text):
    text =text.split('```')[::2]
    response = '.'.join(text)
    language = detect(response)
    tts = gTTS(text=response, lang=language)
    tts.save("response.wav")
    