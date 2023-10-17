import speech_recognition as sr
from gtts import gTTS
import os
import wikipedia

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
hugio = r.recognize_google(audio, language='zh-TW')


wikipedia.set_lang("zh")


summary = wikipedia.summary(hugio)
    

tts = gTTS(summary,lang="zh-TW")
tts.save("aa.mp3")
os.system("mpg123 aa.mp3")
