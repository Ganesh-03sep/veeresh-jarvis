import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os

# Text-to-Speech Engine Initialization
engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    st.info(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        st.success(f"You said: {query}")
    except:
        speak("Sorry, I didn't catch that. Please say again.")
        return "None"
    return query.lower()

def process_query(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(result)

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "play" in query:
        song = query.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif "open code" in query:
        codePath = "C:\\Users\\YourName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak("Opening Visual Studio Code")

    elif "exit" in query or "stop" in query:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("I’m not sure how to help with that.")
    return True

# Streamlit UI
st.title("🧠 Jarvis - Your AI Assistant")
st.write("Click the button below and speak your command")

if st.button("Start Listening"):
    command = take_command()
    if command != "None":
        continue_listening = process_query(command)

st.markdown("---")
st.markdown("""<p style= 'text-align: center;' >Powered by <b>Streamlit</b> and <b>Google Gemini AI</b> | Developed by >> <a href="https://www.linkedin.com/in/veeresh-hajanale-63a587272"  target="_blank" style='text-decoration: none; color: #FFFFFF'><b>veeresh</b></a></p>""", unsafe_allow_html=True)

