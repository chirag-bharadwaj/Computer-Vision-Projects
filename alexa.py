import pywhatkit
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mia' in command:
                command = command.replace('mia', '')
                print(command)
    except:
        pass
    return command


def run_mia():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('current time is' + time)
    elif 'send' in command:
        pywhatkit.sendwhatmsg('+91 6362397215', 'Love from Python', 20, 12)
    elif 'Tell me' in command:
        person = command.replace('Tell me', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("i think you should know that i am a software program developed by you, just a week ago, and moreover, you can't have SEX with me")
    elif 'are you single' in command:
        talk("don't waste your time hitting on me, try someone in J Spider Basvangudi")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I am done with you, leave me alone')


while True:
    run_mia()
