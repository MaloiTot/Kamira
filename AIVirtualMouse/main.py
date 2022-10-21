import warnings
import webbrowser
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
import requests
import jason


warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voice[0].id)
engine.setProperty('voice', voices[2].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)
    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)

    except sr.UnknownValueError:
        print("Assistance could not understand the audio")

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data


def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January"
        "February"
        "March"
        "April"
        "May"
        "June"
        "July"
        "August"
        "September"
        "October"
        "November"
        "December"
    ]

    ordinals = [
        "1st"
        "2nd"
        "3rd"
        "4th"
        "5th"
        "6th"
        "7th"
        "8th"
        "9th"
        "10th"
        "11th"
        "12th"
        "13th"
        "14th"
        "15th"
        "16th"
        "17th"
        "18th"
        "19th"
        "20th"
        "21st"
        "22th"
        "23rd"
        "24th"
        "25th"
        "26th"
        "27th"
        "28th"
        "29th"
        "30th"
        "31st"
    ]
    return 'Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.'


def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello", "howdy", "what's good", "hey there"]

    response = ["hi", "hey", "hola", "greetings", "wassup", "hello", "howdy", "what's good", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."
    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 2 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(";", "-") + "-note.txt"
    with open(file_name, "n") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

while True:

    try:

        text = rec_audio()
        speak = " "

        if call(text):
            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridien = ""
                if now.hour >= 12:
                    meridien = "p.m"
                    hour = now.hour - 12
                else:
                    meridien = "a.m"
                    hour = now.hour
                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridien + " ."

            elif "wikipedia" in text or "wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            elif "who are you" in text or "define yourself" in text:
                speak = speak + """ Hello, I am Smart Kamira your assistant. I exist to make your life easier."""

            elif "your name" in text:
                speak = speak + "my name is Smart Kamira"

            elif "who am I" in text:
                speak = speak + "you must be a human"

            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "It is a secrete"

            elif "how are you" in text:
                speak = speak + "I am amazing, thank you"
                speak = speak + "\nHow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that you are fine"

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )
            elif "youtube" in text.lower():
                speak = speak + "Opening Youtube"
                webbrowser.open("https://youtube.com/")
            else:
                speak = speak + "Application not available"

        elif "youtube" in text.lower():
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "https://www.youtube.com/results?search_query" +
                "+". join(search)
            )
            speak = speak + "Opening" + str(search) + " on youtube"

        elif "search" in text.lower():
            ind = text.lower().split().index("search")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "https://www.google.com/search?q" + "+".join(search)
            )
            speak = speak + "Searching " + str(search) + " on google"

        elif "google" in text.lower():
            ind = text.lower().split().index("google")
            search = text.split()[ind + 1:]
            webbrowser.open(
                "https://www.google.com/search?q=" + "+".join(search)
            )
            speak = speak + "Searching " + str(search) + " on google"

        elif "play music" in text or "play song" in text:
            talk("Here you go with music")
            music_dir = r'C:\Users\mfund'
            songs = os.listdir(music_dir)
            d = random.choice(songs)
            random = os.path.join(music_dir, d)
            playsound.playsound(random)

        elif "empty recycle bin" in text:
            winshell.recycle_bin().empty(
                confirm=True, show_progress=False, sound=True
            )
            speak = speak + "recycle bin emptied "


        elif "note" in text or "remember this" in text:
            talk("what would you like me to write down?")
            note_text = rec_audio()
            note(note_text)
            speak = speak + "I have made a note of that"

        elif "joke" in text or "jokes" in text:
            speak = speak + pyjokes.get_joke()

        elif "weather" in text:
            key = ""
            weather_url = "http://api.openweathermap.org/data/2.5/weather?"
            ind= text.split().index("in")
            location = text.split()[ind + 1:]
            location = "".join(location)
            url = weather_url + "appid" + key + "&q=" + location
            js = requests.get(url).json()
            if js["cod"] != "404":
                weather = js["main"]
                temperature = weather["temp"]
                temperature = temperature - 273.15
                humidity = weather["humidity"]
                desc = js["weather"][0]["description"]
                weather_response = "The temperature in Celcius is " + str(temperature) + "The humidity is"
                + str(humidity) + " and weather description is" + str(desc)
                speak = speak + weather_response
            else:
                speak = speak + "City not found"


            response(speak)

    except:
        talk("I dont know that")

