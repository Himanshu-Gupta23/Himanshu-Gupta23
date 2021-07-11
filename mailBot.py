from email import message
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            # print('>>>>>>>')
            return info.lower()

    except:
        pass

def send_email(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('find.singhal@gmail.com', 'find@gmail')

    email = EmailMessage()
    email['From'] = 'find.singhal@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)

email_list = {
    'ok': 'singhal.himanshu210@gmail.com',

}

def get_email_info():
    talk('To whom you want to send mail')
    name = get_info()
    print(name)
    receiver = email_list.get(name)
    # print(receiver)
    talk('What is the subject of your mail')
    subject = get_info()
    talk('What is the main content of your mail')
    content = get_info()
    send_email(receiver, subject, content)
    talk('Email sent succssfully')
    talk('Do you want to send another Email?')
    send_another = get_info()
    if 'yes' in send_another:
        get_email_info()


get_email_info()

