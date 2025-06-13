"""This code listens for user input using the speech recognition engine."""

import speech_recognition as sr
from speak import speak


def listen():
    """
    Listens for user input using the speech recognition engine.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("I'm sorry, I didn't understand that.")
        return None
    except sr.RequestError as e:
        speak("Sorry, there was an error with the speech recognition service.")
        print(f"Error: {e}")
        return None
