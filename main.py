from AssistantPackage import talkAssistant, runCommand

if __name__ == '__main__':
    try:
        talkAssistant.Talk("Hey I'm your virtual assistant, How can i help you?")
        bool = True

        while bool:
            bool = runCommand.RunAssistant()
    except:
        pass
