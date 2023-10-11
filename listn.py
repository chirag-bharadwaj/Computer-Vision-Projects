import pyttsx3

def onStart():
    print('starting')

def onWord(name, location, length):
    print('word', name, location, length)

def onEnd(name, completed):
    print('finishing', name, completed)

engine=pyttsx3.init()
engine.setProperty("rate", 130)
# engine.setProperty("volume", 1)
engine.setProperty("voice", 1)
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

sen='its me chirag Bharadwaj'

engine.say(sen)
engine.runAndWait()
