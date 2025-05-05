import pyjokes
import pyttsx3

joke = pyjokes.get_joke()
print(joke)

engine = pyttsx3.init()
engine.say("Its working fine")
engine.runAndWait()