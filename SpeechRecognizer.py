"""  =================================================================
File: SpeechRecognizer.py
This file contains code for the SpeechRecognizer class that can convert
the user's speech into text.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
 ==================================================================="""

import speech_recognition as sr


class SpeechRecognizer:
    """Represents a speech recognizer object"""

    def __init__(self):
        """Sets up a speech recognizer object"""
        self.recognizer = sr.Recognizer()

    def getSpeech(self, prompt):
        """Records the user's speech and turn it into text form"""
        # Obtains audio from the microphone
        with sr.Microphone() as source:
            print(prompt)
            audio = self.recognizer.listen(source)

        # Recognizes speech using Google Speech Recognition
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            return None
