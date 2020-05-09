"""  =================================================================
File: KuriProgram.py

This file contains code that implements the GUI for the Kuri robot.

Authors: Anh Nguyen, Lily Irvin, Ryan Specht
 ==================================================================="""

import time
import random
from tkinter import *
# import Image, ImageTk
import numpy as np
import cv2

from KuriBot import KuriBot
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
        self.kuri = KuriBot("neutral")

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
        # mainloop()

    def useSpeech(self):
        self.root.destroy()
        self.sr = SpeechRecognizer()
        # self.kuri.runKuri()
        txt = self.sr.getSpeech("Talk to me! (Press 'q' to quit) ")
        while True:
            # TODO: fix key press
            self.root.bind("<KeyPress>", self.quitKey)
            if txt:
                sentiment = self.sd.getSentiment(txt)
                self.kuri = KuriBot(sentiment.lower())
                self.kuri.runKuri()
                txt = self.sr.getSpeech("Talk to me! (Press 'q' to quit) ")
            else:
                txt = self.sr.getSpeech("Could you say that again? (Press 'q' to quit) ")

    def useChat(self):
        self.root.destroy()
        # self.kuri.runKuri()
        txt = input("Talk to me! (Press 'q' to quit) ")
        while True:
            if txt == 'q':
                quit()
            else:
                sentiment = self.sd.getSentiment(txt)
                self.kuri = KuriBot(sentiment.lower())
                self.kuri.runKuri()
                txt = input("Talk to me! (Press 'q' to quit) ")

    def quitKey(e):
        if e == 'q':
            quit()

    # def _initMessage(self):
    #     """Sets up the section of the window where messages appear, errors, failures, and numbers
    #     about how much work was done"""
    #     messageFrame = Frame(self.root, bd=5, padx=10, pady=10, relief="groove")
    #     messageFrame.grid(row=2, column=2, padx=5, pady=5)
    #     self.messageVar = StringVar()
    #     self.messageVar.set("")
    #     message = Label(messageFrame, textvariable=self.messageVar, width=60, height=3, wraplength=300)
    #     message.grid(row=1, column=1)


def RunKuriProgram():
    """This starts it all up.  Sets up the KuriGUI, and its widgets, and makes it go"""
    k = KuriGUI()
    k.welcomeScreen()
    # s.setupWidgets()
    # s.goProgram()


# The lines below cause the maze to run when this file is double-clicked or sent to a launcher, or loaded
# into the interactive shell.
if __name__ == "__main__":
    RunKuriProgram()
    mainloop()
