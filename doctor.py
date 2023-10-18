import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
from gtts import gTTS
import os
import time

tts = gTTS("請問您有甚麼症狀",lang="zh-TW")
tts.save("aa.mp3")
os.system("mpg123 aa.mp3")
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source,timeout=5)
text = r.recognize_google(audio, language='zh-TW')
tts = gTTS("持續幾天",lang="zh-TW")
tts.save("aa.mp3")
os.system("mpg123 aa.mp3")
time.sleep(4)
tts = gTTS("有沒有否服用其他藥物 請回復有或沒有",lang="zh-TW")
tts.save("aa.mp3")
os.system("mpg123 aa.mp3")
with sr.Microphone() as source:
    audio = r.listen(source,timeout=5)
med = r.recognize_google(audio, language='zh-TW')
if med =="有":
    tts = gTTS("甚麼藥名",lang="zh-TW")
    tts.save("aa.mp3")
    os.system("mpg123 aa.mp3")
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=5)
    medname = r.recognize_google(audio, language='zh-TW')
tts = gTTS("稍等 正在分析診斷結果",lang="zh-TW")
tts.save("aa.mp3")
os.system("mpg123 aa.mp3")

data = {
"symptoms":f"{text}",
"duration":"3",
"medications":f"{med}",
"medication_name":f"{medname}",
"food":"no"
}
hea = {"User-Agent":
"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"}

a = requests.post("http://timtimtimtimtim.pythonanywhere.com/%E5%B8%A5tim%E7%B5%90%E6%9E%9C%E5%88%86%E6%9E%90",headers=hea,data = data)

soup = bs4.BeautifulSoup(a.text, 'html.parser')

# 找到具有 class="card-text" 的 <p> 元素
card_text_element = soup.find('p', class_='card-text')

tts = gTTS(card_text_element.string,lang="zh-TW")
tts.save("aa.mp3")
os.system("mpg123 aa.mp3")