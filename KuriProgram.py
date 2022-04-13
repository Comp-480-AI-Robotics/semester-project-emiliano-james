"""  =================================================================
File: KuriProgram.py
This file contains code that runs the command-line interface for the Kuri robot.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
Contributors: Emiliano Huerta, James Yang
 ==================================================================="""
from subprocess import Popen, PIPE
import io

from SentimentDetector import SentimentDetector
from SpeechRecognizer import SpeechRecognizer


class KuriProgram:
    """Sets up and manages all the variables for the program"""

    def __init__(self, proc):
        """Sets up a new sentiment detector and a new speech recognizer and
        asks for communication method"""
        self.sd = SentimentDetector()
        self.sr = SpeechRecognizer()
        self.option = input("Welcome to Kuri! Type 'c' to chat or 's' to speak! ").lower()
        self.proc = proc

    def startKuri(self):
        """Starts the program using chat or speech"""
        if self.option == 'c':
            self.useChat()
        elif self.option == 's':
            self.useSpeech()

    def useChat(self):
        """Displays the Kuri robot and repeatedly takes in user input in text form,
        while continuously updating the robot's face and heart light"""
        # Implements a subprocess to run the Kuri robot simultaneously with the user input loop
        proc_stdin = io.TextIOWrapper(self.proc.stdin, encoding='utf-8', line_buffering=True)

        while True:
            txt = input("Talk to me! (Type 'q' to quit) ").lower()
            if txt == 'q':
                proc_stdin.write('q\n')
                quit()
            else:
                sentiment = self.sd.getSentiment(txt)
                proc_stdin.write(sentiment + '\n')
                print("Sentiment: " + sentiment + '\n')

    def useSpeech(self):
        """Displays the Kuri robot and repeatedly takes in user input in speech form,
        while continuously updating the robot's face and heart light"""
        # Implements a subprocess to run the Kuri robot simultaneously with the user input loop
        proc_stdin = io.TextIOWrapper(self.proc.stdin, encoding='utf-8', line_buffering=True)

        while True:
            prompt = input("Type 's' to begin recording! (Type 'q' to quit) ").lower()
            if prompt == 'q':
                proc_stdin.write('q\n')
                quit()
            if prompt == 's':
                print("How may I help you?")
                self.sr.response(self.sr.getSpeech()) 
                print("Finished processing!")
                if not self.sr.getSpeech():
                    print("\nCould you say that again?")
                else:
                    sentiment = self.sd.getSentiment(self.sr.getSpeech())
                    proc_stdin.write(sentiment + '\n')
                    print("Sentiment: " + sentiment + '\n')


def RunKuriProgram():
    """Sets up the KuriProgram and its widgets and makes it go simultaneously with the KuriBot"""
    proc = Popen(["python KuriBot.py"], shell=True, stdin=PIPE, close_fds=True)
    k = KuriProgram(proc)
    k.startKuri()


if __name__ == "__main__":
    RunKuriProgram()
