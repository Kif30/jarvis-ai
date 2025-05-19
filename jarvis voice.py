import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# 🎤 Initialize recognizer
recognizer = sr.Recognizer()

# 📢 Function to make Jarvis speak using Google TTS
def speak(text):
    print(f"JARVIS: {text}")
    
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en', slow=False)

    # Save to a known safe file path
    file_path = "jarvis_output.mp3"
    tts.save(file_path)

    # Play and delete after
    playsound.playsound(file_path)
    os.remove(file_path)

# 🎧 Function to listen to your command
def listen():
    with sr.Microphone() as source:
        print("🎧 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("No speech detected. Please try again.")
            return ""

        try:
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn’t catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, the speech service is down.")
            return ""

# 🚀 Startup Message
speak("Hello Boss. I am Jarvis. Ready to assist you.")

# 🔁 Main Loop
while True:
    command = listen()

    if command == "":
        continue

    if "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye Boss. Shutting down.")
        break
    elif "your name" in command:
        speak("I am Jarvis. Just a rather very intelligent system.")
    elif "hello" in command:
        speak("Hello Boss! It's a pleasure.")
    elif "how are you" in command:
        speak("I am operational and ready to help.")
    else:
        speak("You said: " + command)
