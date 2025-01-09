import pyttsx3, speech_recognition as sr, datetime, wikipedia as wp, webbrowser, os ##I download some needed library for this project  
             ####### TEXT---TO---SPEECH #######
# Taking voice from my system
engine = pyttsx3.init('sapi5')  # "engine" the name of patten
voices = engine.getProperty('voices') #Note= getProperty('voices')= mean we get the (voices) property from pyttsx3.init.    
#print(voices[1].id)

engine.setProperty('voice', voices[1].id) # all set, we get voices-property from pyttsx3 and we use (setProperty)
engine.setProperty('rate',120)

# speak voice function

## when we get 2 thing for voice function then [which 2 function {getProperty},{setProperty}]
def speak(text):
    '''This function takes text and returns a voice
    '''
    engine.say(text)
    engine.runAndWait()

#speak('hello Love, How are you? I am in love with you sweety ')

               #####SPEECH---TO---TEXT#######

#speech-recognition-function

def takeCommand():
    '''This function takes voice from user and returns it as text
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source: #->*
        print('Listening...') # listening means when we are talking write now ... thats why "listening"
        r.pause_threshold = 2 # pause time 1 to 10
        audio = r.listen(source) #->*
        
        try:
            print('Recognizing...') # your command listening your voice, now you talk 
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "none"
        return query

text= takeCommand()        
speak(text)