import speech_recognition as sr

try:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source,timeout=5)
	a = r.recognize_google(audio, language='zh-TW')
	print(a)
	
except:
	print("no")
if a == "03":
	print("yes")
