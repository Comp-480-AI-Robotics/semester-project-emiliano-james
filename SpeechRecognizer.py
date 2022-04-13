"""  =================================================================
File: SpeechRecognizer.py
This file contains code for the SpeechRecognizer class that can convert
the user's speech into text.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
Contributors: Emiliano Huerta, James Yang
 ==================================================================="""
from time import ctime
import time
import speech_recognition as sr
import gtts as gTTS 
import playsound
import os
import random



class SpeechRecognizer:
    """Represents a speech recognizer object"""

    def __init__(self):
        """Sets up a speech recognizer object"""
        self.recognizer = sr.Recognizer()

    def getSpeech(self):
        """
        Records the user's speech and turn it into text form

        Returns:
            audio: the voice input from a user
        """
        # Obtains audio from the microphone
        with sr.Microphone() as source:
            # we are defining our orignal voice data to nothing 
            audio = self.recognizer.listen(source)
        # Recognizes speech using Google Speech Recognition
        try:
            print(self.recognizer.recognize_google(audio))
            audio = self.recognizer.recognize_google(audio)
            return audio

        except sr.UnknownValueError:
            self.kuri_speak("Sorry, I was unable to process what you said. Please try again")
            return None
        except sr.RequestError as e:
            self.kuri_speak("Sorry, I am unable to connect to the internet at this moment. Please try again later")
            return None


    def response(self, voice_data):
        """
        This function serves as the response interpretation from each user voice input which scan the voice data and checks to see if any
        words that it may recognize are present

        Args:
            voice_data (string): this argument is a voice input that is converted to string to allow kuri to interpret and respond
        """
        if voice_data is not None: 
            if 'what is your name' in voice_data:
                self.kuri_speak("My name is Kuri")
            if 'time is it' in voice_data:
                self.kuri_speak(ctime())
            if "exit" in voice_data | 'goodbye kuri' in voice_data | 'leave kuri' in voice_data: 
                self.kuri_speak("Ok, Goodbye")
                quit() 
            time.sleep(1)
            while 1:
                voice_data = self.getSpeech() 
                self.response(voice_data)


    def kuri_speak(self, audio_string): 
        """
        This function uses google's text to speech module in order to convert the text message kuri generates to speech

        Args:
            audio_string (string): audio_string is a string that when passed to google's tts it is spoken 
        """
        tts = gTTS.gTTS(text=audio_string, lang='en')
        randomNum = random.randint(1,100000)
        audio_file = 'audio-' + str(randomNum) + '.mp3'
        tts.save(audio_file) 
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)
