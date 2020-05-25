import time
import speech_recognition as sr

command = ''

# this is called from the background thread
def callback(recognizer, audio):
    # Recognize speech
    try:
        # Uses gog speech recog with 'default API key' please input your own please
        said = recognizer.recognize_google(audio)
        print('Chad has interpreted your speech: You have said: ' + said)
        global command
        command = said
    except sr.UnknownValueError:
        print('Chad did not understand.')
    except sr.RequestError as e:
        print('Chad error; {0}'.format(e))

# Get audio from mic
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # only need to calibrate once before listening
    
# start listening in background (not in 'with')
stop_listening = r.listen_in_background(m, callback)
# stop_listening is now a function that stops background listening when invoked


# this is the good loop
isCommand = False
while True:
    speech = command.lower()
    
    if not isCommand:
        if 'chad' in speech:
            print("I'm listening.")
            isCommand = True
            # we are now listening for commands
    else:
        # There are commands
        isCommand = False
        words = speech.partition(' ')
        
        if words[0] == 'add':
            print(words[1] + words[2])
            pass
        elif words[0] == 'lights':
            if words[1] == 'on':
                print('now you can see')
            else:
                print('you can NOT see you blind fool. You should have done the right thing. I hate you.')
    
        
    # STOP
    if speech == 'stop':
        stop_listening(wait_for_stop=False)
        break

print('stoped')