import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",rate-100)
engine.say("please enter your mail id !")
engine.runAndWait() ;
with sr.Microphone() as source:
    print("say somrthing")
    audio=r.listen(source)
    print("Done!")
txt = r.recognize_google(audio, language='en-us')
print(txt)

list_string = txt.split(' ')
txt = ''.join(list_string)
print(txt)
engine.say(txt)
engine.runAndWait() ;

