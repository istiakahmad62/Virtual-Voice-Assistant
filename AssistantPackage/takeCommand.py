import speech_recognition as sr

def TakeCommand():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey' in command:
                return command
    except:
        pass