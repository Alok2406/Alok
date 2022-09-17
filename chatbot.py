import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import smtplib



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hours = int(datetime.datetime.now().hour)

    if hours>=0 and hours<12:
        speak("Good Morning")

    elif hours>=12 and hours<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
        
    speak("How May i help u sir")

def takecommand():
    #it take speech input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-IN')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say That again please...")
        return "None"
    
    return query
def sendEmail(to,context):
    server = smtplib.SMTP('smtp.gmail.com',465)
    server.ehlo()
    server.starttls()
    server.login('lootbaaj@gmailcom','ieioiyietbfibcaq')
    server.sendmail('lootbaaj@gmailcom',to, context)
    server.close()


if __name__ == "__main__":
    speak("Hi Jarvis Here your alltime favorite assistant")
    wishme()
    while True:
        query=takecommand().lower()
        #Logic for executing task based on query
        #if your q
        if 'wikipedia'  in query:
            print('Searching On wikipedia')
            speak('Searching On wikipedia')
            query =query.replace('wikipedia',"")
            results= wikipedia.summary(query, sentences=3)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\\songs\\Songs'
            Songs= os.listdir(music_dir)
            print(Songs)
            os.startfile(os.path.join(music_dir,Songs[0]))
            #random.choice('abcde') for _ in range(3)
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir,the time is{strtime}")

        elif 'open code' in query:
            codePath= "C:\\Users\\Alok\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("What should i say ?")
                context = takecommand()
                to = "motgharealok@gmail.com"
                sendEmail(to,context)
                speak("Email has been sent...!")
            
            except Exception as e:
                print(e)
                speak("We went into a problem and Email hasn't been sent.!")

        elif 'quit' in query:
            speak("Thanx for using Jarvis")
            exit()