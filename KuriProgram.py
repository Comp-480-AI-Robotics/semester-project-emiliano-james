"""  =================================================================
File: KuriProgram.py
This file contains code that implements the GUI for the Kuri robot.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
 ==================================================================="""

from tkinter import *
from subprocess import Popen, PIPE
import io

from SentimentDetector import SentimentDetector
from SpeechRecognizer import SpeechRecognizer


class KuriGUI:
    """Set up and manage all the variables for the GUI interface."""

    def __init__(self):
        """Set up a new Tk object of the right size"""
        self.root = Tk()
        self.root.title("Kuri Program")
        self.canvas = None
        self.canvasSize = 300
        self.canvasPadding = 10
        self.sd = SentimentDetector()

    def welcomeScreen(self):
        self.welcome = Canvas(self.root,
                             width=self.canvasSize + self.canvasPadding,
                             height=self.canvasSize + self.canvasPadding)
        self.welcome.grid(row=1, column=1)
        buttonFrame = Frame(self.root, bd=5, padx=5, pady=5)
        self.speechButton = Button(buttonFrame, text="Speak", command=self.useSpeech)
        self.chatButton = Button(buttonFrame, text="Chat", command=self.useChat)
        self.speechButton.grid(row=0, column=1)
        self.chatButton.grid(row=1, column=1)
        buttonFrame.grid(row=1, column=1)
        print("Welcome!")

    def useSpeech(self):
        self.root.destroy()
        proc = Popen(["python3 KuriBot.py"], shell=True, stdin=PIPE, close_fds=True)
        proc_stdin = io.TextIOWrapper(proc.stdin, encoding='utf-8', line_buffering=True)
        self.sr = SpeechRecognizer()
        txt = self.sr.getSpeech("Talk to me! (Press 'q' to quit) ")
        while True:
            if txt:
                sentiment = self.sd.getSentiment(txt)
                proc_stdin.write(sentiment)
                txt = self.sr.getSpeech("Talk to me! (Press 'q' to quit) ")
            else:
                txt = self.sr.getSpeech("Could you say that again? (Press 'q' to quit) ")

    def useChat(self):
        self.root.destroy()
        proc = Popen(["python KuriBot.py"], shell=True, stdin=PIPE, close_fds=True)
        proc_stdin = io.TextIOWrapper(proc.stdin, encoding='utf-8', line_buffering=True)
        txt = input("Talk to me! (Press 'q' to quit) ")
        while True:
            if txt == 'q':
                proc_stdin.write('q\n')
                quit()
            else:
                sentiment = self.sd.getSentiment(txt)
                proc_stdin.write(sentiment + '\n')
                txt = input("Talk to me! (Press 'q' to quit) ")


def RunKuriProgram():
    """This starts it all up.  Sets up the KuriGUI, and its widgets, and makes it go"""
    k = KuriGUI()
    k.welcomeScreen()


if __name__ == "__main__":
    RunKuriProgram()
    mainloop()

