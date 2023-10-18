import requests
from gtts import gTTS
import os
import json
import speech_recognition as sr


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

