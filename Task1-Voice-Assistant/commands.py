import datetime
import webbrowser
import os
from google import genai


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}"


def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    return f"Today's date is {current_date}"


def open_google():
    webbrowser.open("https://www.google.com")
    return "Opening Google"


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube"


def ask_ai(question):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question
        )

        return response.text

    except Exception as e:
        print("Gemini error:", e)
        return "Gemini is temporarily unavailable. Please try again."