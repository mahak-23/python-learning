"""
JARVIS - Virtual Assistant
==========================
A sophisticated voice-activated AI assistant

Features:
- OpenAI GPT integration for intelligent responses
- Wake word detection ("Jarvis")  
- Voice synthesis with multiple TTS options
- Web browsing automation
- Music library integration
- News API integration
- Advanced speech recognition
"""

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# Configuration - Replace with your actual API keys
OPENAI_API_KEY = "<Your OpenAI Key Here>"
NEWS_API_KEY = "<Your News API Key Here>"

# Initialize components
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    """Traditional TTS using pyttsx3"""
    engine.say(text)
    engine.runAndWait()

def speak(text):
    """Enhanced TTS using Google Text-to-Speech with pygame playback"""
    try:
        tts = gTTS(text)
        tts.save('temp.mp3')

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Load and play the MP3 file
        pygame.mixer.music.load('temp.mp3')
        pygame.mixer.music.play()

        # Keep the program running until the music stops playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.music.unload()
        os.remove("temp.mp3")
    except Exception as e:
        print(f"TTS Error: {e}")
        # Fallback to traditional TTS
        speak_old(text)

def aiProcess(command):
    """Process commands using OpenAI GPT"""
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
                {"role": "user", "content": command}
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, I'm having trouble processing that request. Error: {str(e)}"

def processCommand(c):
    """Process voice commands and execute appropriate actions"""
    command = c.lower()
    
    # Web browsing commands
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
    
    # Music commands
    elif command.startswith("play"):
        try:
            song = command.split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        except (IndexError, KeyError):
            speak("Sorry, I couldn't find that song or you didn't specify a song name")
    
    # News commands
    elif "news" in command:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                
                speak("Here are the top headlines")
                for i, article in enumerate(articles[:5]):  # Limit to 5 headlines
                    speak(f"Headline {i+1}: {article['title']}")
            else:
                speak("Sorry, I couldn't fetch the news right now")
        except Exception as e:
            speak("There was an error getting the news")
            print(f"News Error: {e}")
    
    # AI-powered responses for everything else
    else:
        output = aiProcess(c)
        speak(output)

def main():
    """Main function"""
    speak("Initializing Jarvis....")
    print("🤖 JARVIS Virtual Assistant")
    print("Say 'Jarvis' to wake me up, then give your command")
    print("=" * 50)
    
    while True:
        # Listen for the wake word "Jarvis"
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    print(f"Command: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            # Didn't recognize speech, continue listening
            pass
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Check if required files exist
    try:
        import musicLibrary
        main()
    except ImportError:
        print("⚠️  musicLibrary.py not found! Creating it now...")
        # Create musicLibrary.py if it doesn't exist
        with open("musicLibrary.py", "w") as f:
            f.write('''# Music Library - Add your favorite songs here
music = {
    "stealth": "https://www.youtube.com/watch?v=U47Tr9BB_wE",
    "march": "https://www.youtube.com/watch?v=Xqeq4b5u_Xw", 
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D",
    "wolf": "https://www.youtube.com/watch?v=ThCH0U6aJpU&list=PLnrGi_-oOR6wm0Vi-1OsiLiV5ePSPs9oF&index=21"
}
''')
        print("✅ musicLibrary.py created! You can now run the assistant.")
        import musicLibrary
        main()