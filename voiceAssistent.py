import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print('voice[1].id')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak('Good Morning...')
    elif hour >= 12 and hour < 15:
        speak('Good Afternoon...')
    else:
        speak('Good Evening...')

    speak('I am KATE. How can I help you?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said = {query}\n")

    except Exception as e:
        print('Say That Again Please...')
        speak('Say That Again Please...')
        return "None"
    return query


if _name_ == '_main_':
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("What should I search in Google,Boss")
            print("What should I search in Google,Boss")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime} Boss")