import requests
import json
import speech_recognition as sr
import pyttsx3
import wikipedia

def sw():
    sweater = {}
    file=requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-E70A78E5-442E-4644-ADB1-6E4715043092")
    data = json.loads(file.text)
    for i in range(len(data["records"]["location"])): 
        sweater[data["records"]["location"][i]["locationName"]]=[data["records"]["location"][i]["weatherElement"][0]["time"][1]["parameter"]["parameterName"]]
        #print(data["records"]["location"][i]["locationName"])
        #print(data["records"]["location"][i]["weatherElement"][0]["time"][1]["parameter"]["parameterName"])
    #a = input("您想知道哪區明日天氣")
    engine.say("您想知道哪一區明日天氣")
    engine.runAndWait()
    with sr.Microphone() as source:
        audio = r.listen(source)
    a = r.recognize_google(audio, language='zh-TW')
    for i in sweater[a]:
        #print(f"{a}明天天氣為{i}")
        engine.say(f"{a}明天天氣為{i}")
        engine.runAndWait()

def dic():
    engine.say("您想查甚麼詞")
    engine.runAndWait()
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio, language='zh-TW')
    wikipedia.set_lang("zh")
    page = wikipedia.page(text)
    summary = wikipedia.summary(text)
    engine.say(summary)
    engine.runAndWait()





while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    hugio = r.recognize_google(audio, language='zh-TW')
    if hugio =="大頭":
        engine = pyttsx3.init()
        engine.say("你好 我是大頭 天氣預報請說天氣   查維基百科請說維基百科")
        engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio, language='zh-TW')
    if text =="天氣":
        sw()
        continue
    elif text =="維基百科":
        dic()
        continue

