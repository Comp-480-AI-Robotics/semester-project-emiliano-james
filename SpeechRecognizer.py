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
#imports for jokes 
import pyjokes




class SpeechRecognizer:
    """Represents a speech recognizer object"""

    def __init__(self):
        """Sets up a speech recognizer object"""
        self.recognizer = sr.Recognizer()
        self.searchBank =  {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how"}
        self.recognizer.energy_threshold = 300
    
    def getSpeech(self):
        """
        Records the user's speech and turn it into text form

        Returns:
            audio: the voice input from a user
        """
        # Obtains audio from the microphone
        with sr.Microphone() as source:
            # we are defining our orignal voice data to nothing 
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
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


    def response(self, voice_data):
        """
        This function serves as the response interpretation from each user voice input which scan the voice data and checks to see if any
        words that it may recognize are present

        Args:
            voice_data (string): this argument is a voice input that is converted to string to allow kuri to interpret and respond
        """
        if voice_data is not None: 
            if "your name" in voice_data:
                self.kuri_speak("My name is Kuri")
            elif "what time is it" in voice_data:
                self.kuri_speak(datetime.now().strftime("%I:%M:%S"))
                # self.kuri_speak(current_time)
            elif "goodbye" in voice_data: 
                self.kuri_speak("Ok, Goodbye")
                quit() 
            elif "weather" in voice_data:
                self.grabWeather() 
            elif "joke" in voice_data:
                self.grab_joke()
            elif "news" in voice_data:
                self.grabNews() 
            elif "sports" in voice_data:
                self.grabSport() 

            while 1:
                voice_data = self.getSpeech() 
                self.response(voice_data)

    def grabWeather(self):
        """
        Summary: This functions makes and api request call to weather api passing it parameters of the requested city gathering 
                weather data and returning it as a string for kuri to report back to the user 
        """
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

        response_2 = requests.get(forecast_url)
        response_2.raise_for_status()

        forecast_data = json.loads(response_2.text)
        # now = datetime.now()
        # current_time = int(now.strftime("%I"))

        temperature = forecast_data['properties']['periods'][0]['temperature']
        shortForecast = forecast_data['properties']['periods'][0]['shortForecast']
        self.kuri_speak("The forcast today is " + str(temperature)+ 'Fahrenheit' + "and weather is" + shortForecast)
        self.kuri_speak("Is there anything else I can help you with?")

    def grab_joke(self, language="en"):
        """
        Summary: This functions returns a joke that is withing the 3 following categories: neutral, twister, or all 

        Args:
            language (str, default): This string defaults the language to english. can be changed to a different lagnauge. Defaults to "en".
        """
        self.kuri_speak("What catergory would you like to hear: neutral, twister, or all")
        jokeType = self.getSpeech() 
        joke = pyjokes.get_joke(language, str(jokeType))
        self.kuri_speak(str(joke))
        self.kuri_speak("Is there anything else I can help you with?")

    def grabNews(self):
        """
        Summary: This functions make a query search to bbc-news gathering the top stories which will be returned and read to the user by Kuri
        """
        # BBC news api
        # following query parameters are used
        # source, sortBy and apiKey
        # we should source this api key to somewhere else so it isnt seen in the file -- fine for now 
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "f2977f6aa47c40f2bba4dd1051c5d3f8" 
        }

        main_url = " https://newsapi.org/v1/articles"
        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        # getting all articles in a string article
        article = open_bbc_page["articles"]
        # empty list which will
        # contain all trending news
        results = []
        for ar in article:
            results.append(ar["title"])
        for i in range(5):
            # speak all trending news top 10 results 
            self.kuri_speak(str(results[i]))
        self.kuri_speak("is there anything else I can help you with?")

    def grabSport(self):
        """
        Summary: This functions make a query search to bbc-news gathering the top stories which will be returned and read to the user by Kuri
        """
        # BBC news api
        # following query parameters are used
        # source, sortBy and apiKey
        # we should source this api key to somewhere else so it isnt seen in the file -- fine for now 
        query_params = {
        "source": "ESPN",
        "country": "us",
        "category": "sports",
        "apiKey": "f2977f6aa47c40f2bba4dd1051c5d3f8" 
        }

        main_url = " https://newsapi.org/v2/top-headlines"
        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        print(res)

        open_bbc_page = res.json()
        # getting all articles in a string article
        article = open_bbc_page["articles"]
        # empty list which will
        # contain all trending news
        results = []
        for ar in article:
            results.append(ar["title"])
        for i in range(5):
            # speak all trending news top 10 results 
            self.kuri_speak(str(results[i]))
        self.kuri_speak("is there anything else I can help you with?")






