from logging import exception
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import subprocess
import pyfiglet

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine. setProperty("rate", 178)
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="en-in")
            print(command)
    except Exception:
       print(Exeption)
    return command



def run_jarvis():
    command = take_command().lower()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The time is " + time)
        print(time)

    elif "about" in command:
        person = command.replace("about" , "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
    
    elif "instagram" in command:
        webbrowser.open("https://instagram.com")

    elif "joke" in command:
        talk(pyjokes.get_joke)

    elif "how are you" in command:
        talk("I am doing good, Boss")




def wishMe():
    print(pyfiglet.figlet_format("J . A . R . V . I . S  HERE ! !"))
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning")
    elif hour>=12 and hour<18:
        talk("Good afternoon")
    else:
        talk("Good evening")

    talk("Jarvis here. How may I help you?")



wishMe()
run_jarvis()
