import pyttsx3

voice_assitant = pyttsx3.init()

def Talk(text):
    voice_assitant.say(text)
    voice_assitant.runAndWait()