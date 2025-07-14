# Initialize text-to-speech engine
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import psutil
import os
import sys

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name} - {voice.id}")
desired_index = 1  # Set this to the index of the desired voice (e.g., 0 or 1)

if len(voices) > 1:
    engine.setProperty('voice', voices[desired_index].id)
else:
    engine.setProperty('voice', voices[0].id)


def talk(text):
    print("🎙 Zyra:", text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Try microphone first, then allow typed input if voice fails."""
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎧 Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)
        try:
            command = listener.recognize_google(voice)
            command = command.lower()
            print("🗣 You said:", command)
            return command
        except sr.UnknownValueError:
            talk("Sorry bro, I didn’t catch that.")
            return ""
        except sr.RequestError:
            talk("Network issue with Google service.")
            return ""
    except Exception as e:
        talk("Mic error. You can type your command instead.")
        print(f"[Mic Error] {e}")
        return input("⌨ Type your command here: ").lower()


def test_voice(index, rate):
    engine.setProperty('voice', voices[index].id)
    engine.setProperty('rate', rate)
    engine.say(f"Hi! I'm Zyra, speaking at rate {rate}.")
    engine.runAndWait()


test_voice(1, 180)  # Example use


def run_zyra():
    command = take_command()

    if command == "":
        return

    if "play" in command:
        song = command.replace("play", "").strip()
        talk("Playing on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "who is uday codes" in command or "who is uday_codes" in command:
        info = (
            "Uday, known as uday_codes on Instagram, is a coding content creator. "
            "He teaches Python projects in Telugu and runs udaycodes.in 💻"
        )
        talk(info)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("Too many matches. Please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn’t find information about that person.")
        except Exception:
            talk("Something went wrong while fetching Wikipedia info.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        ]
        for path in chrome_paths:
            if os.path.exists(path):
                talk("Opening Chrome 🚀")
                os.startfile(path)
                return
        talk("Chrome path not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()

    else:
        talk("I heard you, but I don’t understand that yet 😅")


talk("Yo! I'm Zyra – your personal voice assistant 💡")
try:
    while True:
        run_zyra()
except KeyboardInterrupt:
    talk("Zyra is shutting down. Bye 👋")
    sys.exit()
