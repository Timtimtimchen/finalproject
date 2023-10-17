from gtts       import gTTS
import os
import wikipedia

wikipedia.set_lang("zh")


summary = wikipedia.summary("靜宜大學")
    

tts = gTTS(summary,lang="zh-TW")
tts.save("aa.mp3")
os.system("mpg123 aa.mp3")
