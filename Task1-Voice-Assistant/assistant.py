import speech_recognition as sr
import pyttsx3

from commands import (
    tell_time,
    tell_date,
    open_google,
    open_youtube,
    ask_ai
)

from config import ASSISTANT_NAME


# Text-to-speech
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# Voice input
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            print("No voice detected.")
            return ""

        except sr.UnknownValueError:
            print("Could not understand.")
            speak("Sorry, I could not understand you.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""


# Execute commands
def run_command(command):

    if "time" in command:
        speak(tell_time())

    elif "date" in command:
        speak(tell_date())

    elif "open google" in command:
        speak(open_google())

    elif "open youtube" in command:
        speak(open_youtube())

    elif "stop" in command or "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False

    else:
        # Any other question → Gemini AI
        print("Thinking...")
        answer = ask_ai(command)
        speak(answer)

    return True


# Start assistant
speak(f"Hello! I am {ASSISTANT_NAME}. How can I help you?")

while True:

    command = listen()

    if command:
        if not run_command(command):
            break