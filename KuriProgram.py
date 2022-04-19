"""  =================================================================
File: KuriProgram.py
This file contains code that runs the command-line interface for the Kuri robot.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
Contributors: Emiliano Huerta, James Yang
 ==================================================================="""
from subprocess import Popen, PIPE
import io
import time

from SentimentDetector import SentimentDetector
from SpeechRecognizer import SpeechRecognizer
from FacialRecognition import FacialRecognizer


class KuriProgram:
    """Sets up and manages all the variables for the program"""

    def __init__(self, proc):
        """Sets up a new sentiment detector and a new speech recognizer and
        asks for communication method"""
        self.sd = SentimentDetector()
        self.sr = SpeechRecognizer()
        self.cap = FacialRecognizer() 
        self.proc = proc

    def startKuri(self):
        """Starts the program using chat or speech"""
        self.useSpeech()

    def useSpeech(self):
        """Displays the Kuri robot and repeatedly takes in user input in speech form,
        while continuously updating the robot's face and heart light"""
        # Implements a subprocess to run the Kuri robot simultaneously with the user input loop
        proc_stdin = io.TextIOWrapper(self.proc.stdin, encoding='utf-8', line_buffering=True)
        # self.cap.captureImage() this is for image processing 
        while True:
            time.sleep(1.5)
            self.cap.cameraCapture() 
            self.sr.kuri_speak("How may I help you?")
            self.sr.response(self.sr.getSpeech()) 
            self.sr.kuri_speak("This is what I found!")
            if not self.sr.getSpeech():
                self.sr.kuri_speak("\nCould you say that again?")
            # else:
            #     sentiment = self.sd.getSentiment(self.sr.getSpeech())
            #     proc_stdin.write(sentiment + '\n')
            #     print("Sentiment: " + sentiment + '\n')


def RunKuriProgram():
    """Sets up the KuriProgram and its widgets and makes it go simultaneously with the KuriBot"""
    proc = Popen(["python KuriBot.py"], shell=True, stdin=PIPE, close_fds=True)
    k = KuriProgram(proc)
    k.startKuri()


if __name__ == "__main__":
    RunKuriProgram()
