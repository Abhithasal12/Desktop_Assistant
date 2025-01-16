import pyttsx3, speech_recognition as sr, datetime, wikipedia as wp, webbrowser, os ##I download some needed library for this project  
             ####### TEXT---TO---SPEECH #######
# Taking voice from my system
engine = pyttsx3.init('sapi5')  # "engine" the name of patten
voices = engine.getProperty('voices') #Note= getProperty('voices')= mean we get the (voices) property from pyttsx3.init.    
#print(voices[1].id)

engine.setProperty('voice', voices[1].id) # all set, we get voices-property from pyttsx3 and we use (setProperty)
engine.setProperty('rate',140)

# speak voice function

## when we get 2 thing for voice function then [which 2 function {getProperty},{setProperty}]
def speak(text):
    '''This function takes text and returns a voice
    '''
    engine.say(text)
    engine.runAndWait()

#speak('hello Thasal, How are you? I am in love with you sweety ')

               #####SPEECH---TO---TEXT#######

#speech-recognition-function

def takeCommand():
    '''This function takes voice from user and returns it as text
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source: #->*
        print('Listening...') # listening means when we are talking write now ... thats why "listening"
        r.pause_threshold = 3 # pause time 1 to 10
        audio = r.listen(source) #->*
        
        try:
            print('Recognizing...') # your command listening your voice, now you talk 
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:        #Note:-this is a councept when we use try and except (exception)
            print("Say that again please...")
            return "none"
        return query
    

        

#text= takeCommand()        
#speak(text)

#The function for wish me by using time

def wishMe():

    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Abhishek!, how are you?")

    elif hour>=12 and hour<18:
        speak("Good afternoon Abhishek!,Whatever action is performed by a great man, common men follow. And whatever standards he sets by exemplary acts, all the world pursues.")

    else:
        speak("Good evening Abhishek!, Of all sciences, I am the spiritual science of the self; and among logicians, I am the conclusive truth")

    speak("I am Nandu, Tell me how can i help you") 



if __name__ == "__main__": #main function
    
    wishMe()

    while True:
   
        query = takeCommand().lower()

            
        if "wikipedia" in query:   #say last [according to Wikipedia]
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wp.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:         ##elif conditiona used for many queries.
            speak("opening youtube......")
            webbrowser.open("youtube.com")

        elif "github" in query:
            speak("opening github......")
            webbrowser.open("github.com")

        elif "music" in query:
            speak("Ok sir, playing music......")
            music_dir = "D:\\Abhishek\\Abhi_Code\\FSDI_GEN-AI\\Py_test\\Desktop_Assistant\\Music" # this is my music directory
            songs = os.listdir(music_dir)
            print(songs)
            speak("I have found some songs. Please select a song")
            os.startfile(os.path.join(music_dir,songs[0]))

        
        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sure, the current time is {strtime}")    

        elif "ok bye" in query:
            speak("Thanks for using me, bye bye!")
            exit()