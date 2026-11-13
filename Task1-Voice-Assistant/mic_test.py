import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=2)

    print("Speak now...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand your voice.")

except sr.RequestError as e:
    print("Speech service error:", e)