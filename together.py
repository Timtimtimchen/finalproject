import speech_recognition as sr
from gtts import gTTS
import os
import wikipedia
import requests
import json
import time
import bs4

def sweater():
    sweater = {}
    file=requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-E70A78E5-442E-4644-ADB1-6E4715043092")
    data = json.loads(file.text)
    for i in range(len(data["records"]["location"])): 
        sweater[data["records"]["location"][i]["locationName"]]=[data["records"]["location"][i]["weatherElement"][0]["time"][1]["parameter"]["parameterName"]]
        #print(data["records"]["location"][i]["locationName"])
        #print(data["records"]["location"][i]["weatherElement"][0]["time"][1]["parameter"]["parameterName"])
    #a = input("您想知道哪區明日天氣")
    tts = gTTS("您想知道哪區明日天氣",lang="zh-TW")
    tts.save("aa.mp3")
    os.system("mpg123 aa.mp3")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=5)
    a = r.recognize_google(audio, language='zh-TW')
    for i in sweater[a]:
        #print(f"{a}明天天氣為{i}")
        tts = gTTS(f"{a}明天天氣為{i}",lang="zh-TW")
        tts.save("aa.mp3")
        os.system("mpg123 aa.mp3")

def wiki():
    tts = gTTS("您想查甚麼詞",lang="zh-TW")
    tts.save("aa.mp3")
    os.system("mpg123 aa.mp3")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,timeout=5)
    text = r.recognize_google(audio, language='zh-TW')
    wikipedia.set_lang("zh")
    summary = wikipedia.summary(text)
    tts = gTTS(summary,lang="zh-TW")
    tts.save("aa.mp3")
    os.system("mpg123 aa.mp3")

def doctor():
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