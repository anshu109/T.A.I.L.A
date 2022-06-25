import datetime
import voice
import time
def greet():
    hour = datetime.datetime.now().hour
    sound=voice.takeinstruction()

    if 'wake up assistant' in  sound:
        if hour > 0 and hour < 12:
            voice.speak("Good Morning sir. How may I help you today?")
        elif hour > 12 and hour < 18:
            voice.speak("Good Afternoon sir, what can i do for you at this time? ")
        else:
            voice.speak("Good evening sir, what can i do for you at this time?")

    else:
        voice.speak("call me in proper way ")
        sound = voice.takeinstruction()
        if 'wake up assistant' in sound:
            if hour > 0 and hour < 12:
                voice.speak("Good Morning sir. How may I help you today?")
            elif hour > 12 and hour < 18:
                voice.speak("Good Afternoon sir, what can i do for you at this time? ")
            else:
                voice.speak("Good evening sir, what can i do for you at this time?")
