from .takeCommand import TakeCommand
from .talkAssistant import Talk

import pywhatkit
import wikipedia
import datetime
import pyjokes

def RunAssistant():
    command = TakeCommand()
    if "stop" in command:
        return False
    else:
        command = command.replace("hey", "")
        if 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            Talk("Current time is " + current_time)
        elif 'play' in command:
            song = command.replace("play", "")
            Talk("Yes, i am playing " + song)
            pywhatkit.playonyt(song)
        elif 'about' in command:
            wiki_query = command.replace("tell me about", "")
            info = wikipedia.summary(wiki_query, 1)
            Talk(info)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            Talk(joke)
        else:
            Talk("Sorry I can't understand, But i search it for you")
            search_query = command
            pywhatkit.search(search_query)
        return True
