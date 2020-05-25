from gtts import gTTS
import speech_recognition as sr
import playsound
from time import sleep
import random
import os

def talk(audio):
    print('An important message from the one and only Chad, the AI produced by Big Roy Studios: '+audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-us')
        text_to_speech.save('audio.mp3')
        playsound.playsound('audio.mp3', True)
        os.remove('audio.mp3')
        
def my_command():
    #Initialize the recognizer 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Chad is Ready...')
        r.pause_threshold = 1
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, duration=1)
        #listens for the user's input
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = my_command();

    return command.lower()

def chad(command):
    errors=[
        "I don\'t know what you mean!",
        "Excuse me?",
        "Can you repeat it please?",
    ]

    if 'hello' in command:
        talk('What\'s good my Brotherernern you can call me Chad, or the ladies call me Chad')

    else:
        error = random.choice(errors)
        talk(error)


talk('Chad! is! ready!')

if __name__ == '__main__':
    while True:
        chad(my_command())
        sleep(3)