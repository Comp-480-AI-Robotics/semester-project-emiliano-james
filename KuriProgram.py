"""  =================================================================
File: KuriProgram.py
This file contains code that runs the command-line interface for the Kuri robot.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
 ==================================================================="""

from subprocess import Popen, PIPE
import io

from SentimentDetector import SentimentDetector
from SpeechRecognizer import SpeechRecognizer


class KuriProgram:
    """Sets up and manages all the variables for the program"""

    def __init__(self):
        """Sets up a new sentiment detector and a new speech recognizer and
        asks for communication method"""
        self.sd = SentimentDetector()
        self.sr = SpeechRecognizer()
        self.option = input("Welcome to Kuri! Type 'c' to chat or 's' to speak! ")

    def startKuri(self):
        """Starts the program using chat or speech"""
        if self.option.lower() == 'c':
            self.useChat()
        elif self.option.lower() == 's':
            self.useSpeech()

    def useChat(self):
        """Displays the Kuri robot and repeatedly takes in user input in text form,
        while continuously updating the robot's face and heart light"""
        # Implements threading to run the Kuri robot simultaneously with the user input loop
        proc = Popen(["python KuriBot.py"], shell=True, stdin=PIPE, close_fds=True)
        proc_stdin = io.TextIOWrapper(proc.stdin, encoding='utf-8', line_buffering=True)

        while True:
            txt = input("Talk to me! (Type 'q' to quit) ")
            if txt.lower() == 'q':
                proc_stdin.write('q\n')
                quit()
            else:
                sentiment = self.sd.getSentiment(txt)
                proc_stdin.write(sentiment + '\n')
                print("Sentiment: " + sentiment + '\n')

    def useSpeech(self):
        """Displays the Kuri robot and repeatedly takes in user input in speech form,
        while continuously updating the robot's face and heart light"""
        # Implements threading to run the Kuri robot simultaneously with the user input loop
        proc = Popen(["python3 KuriBot.py"], shell=True, stdin=PIPE, close_fds=True)
        proc_stdin = io.TextIOWrapper(proc.stdin, encoding='utf-8', line_buffering=True)

        while True:
            prompt = input("Type 's' to begin recording! (Type 'q' to quit) ")
            if prompt.lower() == 'q':
                proc_stdin.write('q\n')
                quit()
            if prompt.lower() == 's':
                txt = self.sr.getSpeech("Recording...")
                print("Finished recording!")
                if not txt:
                    print("\nCould you say that again?")
                else:
                    sentiment = self.sd.getSentiment(txt)
                    proc_stdin.write(sentiment + '\n')
                    print("Sentiment: " + sentiment + '\n')


def RunKuriProgram():
    """Sets up the KuriProgram and its widgets and makes it go"""
    k = KuriProgram()
    k.startKuri()


if __name__ == "__main__":
    RunKuriProgram()
