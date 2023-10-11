import pyttsx3

res = pyttsx3.init()
res.setProperty("rate", 140)

res.say("Good morning Mr. Bharadwaj, how was your last year sir")
res.say("I know this time you're going to get it sir")
res.runAndWait()
