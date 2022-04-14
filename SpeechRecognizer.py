"""  =================================================================
File: SpeechRecognizer.py
This file contains code for the SpeechRecognizer class that can convert
the user's speech into text.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
Contributors: Emiliano Huerta, James Yang
 ==================================================================="""
from datetime import datetime
import time
import speech_recognition as sr
import gtts as gTTS 
import playsound
import os
import random
import requests 
from geopy.geocoders import Nominatim

# imports for grabWeather() method
import requests
import json
# import pandas as pd
# import numpy as np




class SpeechRecognizer:
    """Represents a speech recognizer object"""

    def __init__(self):
        """Sets up a speech recognizer object"""
        self.recognizer = sr.Recognizer()
        self.searchBank =  {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how"}

    def getSpeech(self):
        """
        Records the user's speech and turn it into text form

        Returns:
            audio: the voice input from a user
        """
        # Obtains audio from the microphone
        with sr.Microphone() as source:
            # we are defining our orignal voice data to nothing 
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
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
            elif 'what time is it' in voice_data:
                now = datetime.now()
                current_time = now.strftime("%I:%M:%S")
                self.kuri_speak(current_time)
            elif 'goodbye' in voice_data: 
                self.kuri_speak("Ok, Goodbye")
                quit() 
            elif "weather" in voice_data:
                reportedWeather = self.grabWeather()
                self.kuri_speak(reportedWeather)
                
                # pass ##must implement city location in order to have more accurate results
            elif self.searchBank.values() in voice_data: 
                pass

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

    def grabWeather(self):
        # need to figure out a better way to grab weather 
        geolocator = Nominatim(user_agent="geoapiExercises")
        self.kuri_speak("What city would you like the weather for?")
        cityName = self.getSpeech() 

        location = geolocator.geocode(cityName)
        if location is None:
            self.kuri_speak("I did not get where you are")
        latitude = location.latitude
        longitude = location.longitude

        weather_url = "https://api.weather.gov/points/{0:.4f},{1:.4f}".format(latitude,longitude)
        response = requests.get(weather_url)
        response.raise_for_status()

        info = json.loads(response.text)
        # forecastHourly_url = info["properties"]["forecastHourly"]
        forecast_url = info["properties"]["forecast"]
        print(forecast_url)

        response_2 = requests.get(forecast_url)
        response_2.raise_for_status()

        forecast_data = json.loads(response_2.text)
        # now = datetime.now()
        # current_time = int(now.strftime("%I"))

        temperature = forecast_data['properties']['periods'][0]['temperature']
        shortForecast = forecast_data['properties']['periods'][0]['shortForecast']

        print(str(temperature) + shortForecast)

        weather = "The forcast today is " + str(temperature)+ 'Fahrenheit' + "and weather is" + shortForecast
        return weather
        # res = "http://dataservice.accuweather.com/locations/v1/cities/"+ str(cityName) 
        # postalcode = res['PrimaryPostalCode']
        # print(postalcode)

        
        # page = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/+"+ zip_code +"?apikey=0yiQHtAJwNcrL8kocvXaXyfVXH6guN87&language=en-us&details=false&metric=false")
        
        # print(page)
        # print(page['Text'])

        # self.kuri_speak("The forcast today is " + page['Text'])

    # def search(self, dict, voice_data):
    #     if dict.values() in voice_data:
    #         print(dict.values() )

        # url = "https://www.google.com/search?q="






