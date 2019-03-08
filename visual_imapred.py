import pyttsx3
import speech_recognition as sr
import smtplib
import getpass
from email.mime.text import MIMEText   
from email.mime.multipart import MIMEMultipart

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate+10) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hey there! Tell me your email-id")
#engine.setProperty('volume',1.5)
engine.runAndWait()
print('Speak Email Id')

r=sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    audio=r.listen(source)
    print("done")
txt=r.recognize_google(audio,language='en-us')
txt1=txt.replace('dot','.')
txt2=txt1.replace(' ','')
txt3=txt2.lower()
print('your email id is '+txt3)

engine = pyttsx3.init()
print("tell me about subject")
engine.runAndWait()

r=sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    audio=r.listen(source)
    print("done")
sub=r.recognize_google(audio,language='en')
sub1=sub.capitalize()
print('subject of your mail is '+sub1)

engine = pyttsx3.init()
print("what is body of mail")
engine.runAndWait()

r=sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    audio=r.listen(source)
    print("done")
body=r.recognize_google(audio,language='en')
body1=body.capitalize()
print('body of mail is '+body1)


msg=MIMEMultipart()
msg['Subject']=sub1
msg['From']='Your E_mail'
password='Password'

msg['To']=txt3
#message=input('enter message\n')
text=MIMEText(body1)
msg.attach(text)
s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()   
s.starttls()
s.ehlo()
s.login(msg['From'],password)
s.sendmail(msg['From'],msg['To'],msg.as_string())
s.quit()
print('Logout Successfully')
