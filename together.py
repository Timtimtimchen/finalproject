import speech_recognition as sr
import wikipedia
import requests
import json
import time 
import bs4
import pyttsx3

def sweater():
    sweater = {}
    file=requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-E70A78E5-442E-4644-ADB1-6E4715043092")
    data = json.loads(file.text)
    for i in range(len(data["records"]["location"])): 
        sweater[data["records"]["location"][i]["locationName"]]=[data["records"]["location"][i]["weatherElement"][0]["time"][1]["parameter"]["parameterName"]]
        #print(data["records"]["location"][i]["locationName"])
        #print(data["records"]["location"][i]["weatherElement"][0]["time"][1]["parameter"]["parameterName"])
    #a = input("您想知道哪區明日天氣")
    engine.say("您想知道哪區明日天氣")
    engine.runAndWait()
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=5)
        a = r.recognize_google(audio, language='zh-TW')
    except:
        # tts = gTTS("不好意思 聽不清楚",lang="zh-TW")
        # tts.save("aa.mp3")
        # os.system("mpg123 aa.mp3")
        engine.say("不好意思 聽不清楚")
        engine.runAndWait()
        return
    if "台" in a:
        a = a.replace("台","臺")
    for i in sweater[a]:
        #print(f"{a}明天天氣為{i}")
        # tts = gTTS(f"{a}明天天氣為{i}",lang="zh-TW")
        # tts.save("aa.mp3")
        # os.system("mpg123 aa.mp3")
        engine.say(f"{a}明天天氣為{i}")
        engine.runAndWait()

def wiki():
    # tts = gTTS("您想查甚麼詞",lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say("您想查甚麼詞")
    engine.runAndWait()
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=5)
        text = r.recognize_google(audio, language='zh-TW')
    except:
        # tts = gTTS("不好意思 聽不清楚",lang="zh-TW")
        # tts.save("aa.mp3")
        # os.system("mpg123 aa.mp3")
        engine.say("不好意思 聽不清楚")
        engine.runAndWait()
        return
    wikipedia.set_lang("zh")
    summary = wikipedia.summary(text)
    # tts = gTTS(summary,lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say(summary)
    engine.runAndWait()
def doctor():
    # tts = gTTS("請問您有甚麼症狀",lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say("請問您有甚麼症狀")
    engine.runAndWait()
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=5)
        text = r.recognize_google(audio, language='zh-TW')
    except:
        # tts = gTTS("不好意思 聽不清楚",lang="zh-TW")
        # tts.save("aa.mp3")
        # os.system("mpg123 aa.mp3")
        engine.say("不好意思 聽不清楚")
        engine.runAndWait()
        return
    # tts = gTTS("持續幾天",lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say("持續幾天")
    engine.runAndWait()
    time.sleep(6)
    # tts = gTTS("有沒有否服用其他藥物 請回復有或沒有",lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say("有沒有服用其他藥物 請回復有或沒有")
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=5)
        med = r.recognize_google(audio, language='zh-TW')
    except:
        # tts = gTTS("不好意思 聽不清楚",lang="zh-TW")
        # tts.save("aa.mp3")
        # os.system("mpg123 aa.mp3")
        engine.say("不好意思 聽不清楚")
        engine.runAndWait()
        return
    if med =="有":
        # tts = gTTS("甚麼藥名",lang="zh-TW")
        # tts.save("aa.mp3")
        # os.system("mpg123 aa.mp3")
        engine.say("甚麼藥名")
        engine.runAndWait()
        try:
            with sr.Microphone() as source:
                audio = r.listen(source,timeout=5)
            medname = r.recognize_google(audio, language='zh-TW')
        except:
            # tts = gTTS("不好意思 聽不清楚",lang="zh-TW")
            # tts.save("aa.mp3")
            # os.system("mpg123 aa.mp3")
            engine.say("不好意思 聽不清楚")
            engine.runAndWait()
            return
    # tts = gTTS("稍等 正在分析診斷結果",lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say("稍等 正在分析診斷結果")
    engine.runAndWait()

    data = {
    "symptoms":f"{text}",
    "duration":"3",
    "medications":f"{med}",
    "medication_name":"a酸",
    "food":"no"
    }
    hea = {"User-Agent":
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"}

    a = requests.post("http://timtimtimtimtim.pythonanywhere.com/%E5%B8%A5tim%E7%B5%90%E6%9E%9C%E5%88%86%E6%9E%90",headers=hea,data = data)

    soup = bs4.BeautifulSoup(a.text, 'html.parser')
    
    card_text_element = soup.find('p', class_='card-text')

    # tts = gTTS(card_text_element.string,lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say(card_text_element.string)
    engine.runAndWait()
def hugio():
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            hugio = r.recognize_google(audio, language='zh-TW')
            print(hugio)
        except:
            # tts = gTTS("聽不清楚 如有需求重新叫我",lang="zh-TW")
            # tts.save("aa.mp3")
            # os.system("mpg123 aa.mp3")
            # engine.say("聽不清楚 如有需求重新叫我")
            # engine.runAndWait()
            continue
        if hugio =="大頭" or '大同':
            break
        elif hugio:
            engine.say("聽不清楚 如有需求重新叫我")
            engine.runAndWait()
            continue


while True:
    engine = pyttsx3.init()
    hugio()
    # tts = gTTS("你好 我是大頭 請選擇  零一 天氣預報  零二  查字典 零三 初步診療",lang="zh-TW")
    # tts.save("aa.mp3")
    # os.system("mpg123 aa.mp3")
    engine.say("你好 我是大頭 請選擇  零一 天氣預報  零二  查字典 零三 初步診療")
    engine.runAndWait()
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        text = r.recognize_google(audio, language='zh-TW')
        print(text)
    except:
        # tts = gTTS("聽不清楚 如有需求重新叫我",lang="zh-TW")
        # tts.save("aa.mp3")
        # os.system("mpg123 aa.mp3")
        engine.say("聽不清楚 如有需求重新叫我")
        engine.runAndWait()
        continue

    if text =="零一" or text =="01":
        sweater()
        continue
    elif text =="零二" or text =="02":
        wiki()
        continue
    elif text =="零三" or text =="03":
        doctor()
        continue
