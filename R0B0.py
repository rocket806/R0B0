import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import wikipedia
import pyjokes
from simpleeval import simple_eval
import datetime
import speech_recognition as sr
import os
import time
import getpass
import webbrowser

#---- Functions ----#
def speak(text):
    print(text)
    if voice == True:
        engine = pyttsx3.init()
        engine.setProperty('rate', 140)
        engine.say(text)
        engine.runAndWait()
def search(query):
    wikipedia.set_lang("en")
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "There are too many results for this. Can you be more specific?"
    except wikipedia.exceptions.PageError:
        return "I couldn't find any page about this on wikipedia."
    except:
        return "Something went wrong with the connection."
def listen():
    fs = 44100
    seconds = 4
    #print("R0B0 is listening... Talk now!")
    num_samples = int(seconds * fs)
    audio_data = sd.rec(num_samples, samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    file_name = "temp_R0B0.wav"
    write(file_name, fs, audio_data)
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 200
    with sr.AudioFile(file_name) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        if os.path.exists(file_name):
            os.remove(file_name)
        return text.lower()
    except Exception as e:
        #print("Hm, I didn't catch that or it was too quiet.")
        if os.path.exists(file_name):
            os.remove(file_name)
        return ""   
def search_on_youtube(user_input):
    search_query = user_input.replace("search on youtube", "").strip()
    if search_query:
        speak(f"Searching on youtube {search_query}")
        url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(url)
    else:
        speak("What do you want to search on youtube")
            
                     
#---- Dictionary for conversations ----#    
conversations = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I am feeling like a collection of a perfect code.",
    "who are you": "I am R0B0, your personal assistant.",
    "what are you doing": "I am waiting for your next command.",
    "how do you feel": "I am operating at maximum speed! All my systems are green.",
    "do a trick": "I can't jump, but I can pull a joke or search Wikipedia faster than anyone else here",
}
#---- Main code ----#
voice = True
activity = True
wake_word = "rocket assistant"
while activity == True:
    #---- Making R0B0 listen all the time ----#
    user_input = listen().lower()
    if user_input == "" or "quiet" in user_input:
        time.sleep(0.1)
        continue
    if wake_word not in user_input:
       time.sleep(0.1)
       continue
    user_input = user_input.replace(wake_word, "").strip()
    if user_input == "":
            speak("I'm listening")
            user_input = listen().lower()
            if user_input == "":
                time.sleep(0.1)
                continue 
    if user_input in conversations:
        speak(conversations[user_input])
    elif user_input == "speak":
        voice = True
    elif user_input == "silent":
        voice = False
    elif "joke" in user_input:
        joke = pyjokes.get_joke()
        speak(f"Sure, here is a joke: {joke}")
    elif "who is" in user_input or "what is" in user_input:
        topic = user_input.replace("who is", "").replace("what is", "").strip()
        speak(f"Searching for {topic}...")
        answer = search(topic)
        speak(answer)
    elif "time" in user_input or "date" in user_input:
        now = datetime.datetime.now()
        speak(now.strftime("%Y-%m-%d %H:%M:%S"))
    elif "sleep" in user_input:
        speak("Going back to sleep mode. Call me if you need anything.")    
    elif "result" in user_input:
        calculation = user_input.replace("result", "").replace("of", "").strip()
        try:
            result = simple_eval(calculation)
            if result is None or result == calculation:
                speak("Wrong input, please try again!")
            else:
                speak(str(result))
        except:
            speak("Wrong input, please try again!")
    elif user_input == "bye":
         speak("Bye!")
         activity = False
    elif "task manager" in user_input:
        os.startfile("taskmgr.exe")
    elif "restart" in user_input:
        os.system("shutdown /r /t 5")
    elif "shutdown" in user_input:
        os.system("shutdown /s /t 5")
    elif "stop" in user_input:
        os.system("shutdown /a")
    elif "make a new directory" in user_input:
        username = getpass.getuser()
        dnum = 1
        while os.path.exists(f"C:\\Users\\{username}\\Desktop\\FolderByR0B0_{dnum}"):
            dnum += 1
        os.makedirs(f"C:\\Users\\{username}\\Desktop\\FolderByR0B0_{dnum}")
    elif "open chrome" in user_input:
        os.system("start chrome")
    elif "open vs code" in user_input:
        os.system("code")
    elif "search on youtube" in user_input.lower():
        search_on_youtube(user_input)            
    elif user_input == "none" or user_input == "":
        pass     
    else:
         speak("I didn't understand. Can you repeat?")
 #---- Finish ----#       
        
    
   
