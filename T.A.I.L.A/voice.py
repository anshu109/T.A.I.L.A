
import speech_recognition as sr
import pyttsx3
def speak(audio):

    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    voices = engine.getProperty('voices')
    engine.say(audio)
    engine.runAndWait()


def takeinstruction():
    r = sr.Recognizer()
    for index, name in enumerate(sr.Microphone.list_microphone_names()):

        index, name
    source_1=sr.Microphone(device_index=0)
    source_2=sr.Microphone(device_index=1)
    with source_1 or source_2:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source_1 or source_2, timeout=None, phrase_time_limit=None)
    try:
        print("Recognising......")
        query = r.recognize_google(audio, language='en-in')
        print(f"audio instruction: ", query)

    except Exception as e:
        return "none"
    return query
# if __name__=='__main__':
#     speak('Hello sir, i am a personal A.I Assistant of TECH I.S, and my name is Taaila')