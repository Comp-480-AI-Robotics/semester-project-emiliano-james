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
        # TODO: close first screen completely
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

    #     self.root = Tk()
    #     self.root.title("Susan Fox's Grid World")
    #     self.numRows = dimension
    #     self.numCols = dimension
    #     self.blockPerc = 30.0
    #     self.numSamples = 100
    #     self.MCLIsRunning = False
    #
    # def setupWidgets(self):
    #     """Set up all the parts of the GUI."""
    #     # Create title frame and main buttons
    #     self._initTitle()
    #
    #     # Create control buttons
    #     self._initEditTools()
    #
    #     # Create the maze grid
    #     self._initMazeGrid()
    #
    #     # Create the search frame
    #     self._initLocalizeTools()
    #
    #     # Create the message frame
    #     self._initMessage()
    #
    #     # # Create the legend frame
    #     # self._initLegend()
    #
    #
    # def goProgram(self):
    #     """This starts the whole GUI going"""
    #     try:
    #         while True:
    #             if self.MCLIsRunning:
    #                 self.stepMCL()
    #             self.root.update_idletasks()
    #             self.root.update()
    #     except TclError:
    #         pass  # avoids error on quitting
    #
    # ### =================================================================
    # ### Widget-creating helper functions
    #
    # def _initTitle(self):
    #     """Sets up the title section of the GUI, where the Quit and Help buttons are located"""
    #     titleButtonFrame = Frame(self.root, bd=5, padx=5, pady=5)
    #     titleButtonFrame.grid(row=1, column=1)
    #     quitButton = Button(titleButtonFrame, text="Quit", command=self.quit)
    #     helpButton = Button(titleButtonFrame, text="Help", command=self.showHelp)
    #     quitButton.grid(row=1, column=1, padx=5)
    #     helpButton.grid(row=1, column=2, padx=5)
    #
    #     titleFrame = Frame(self.root, bd=5, padx=5, pady=5)
    #     titleFrame.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
    #
    #     titleLabel = Label(titleFrame, text="Susan Fox's Maze for Localization", font="Arial 20 bold",
    #                        anchor=CENTER, padx=5, pady=5)
    #     titleLabel.grid(row=1, column=1)
    #
    # # end _initTitle
    #
    #
    # def _initMessage(self):
    #     """Sets up the section of the window where messages appear, errors, failures, and numbers
    #     about how much work was done"""
    #     messageFrame = Frame(self.root, bd=5, padx=10, pady=10, relief="groove")
    #     messageFrame.grid(row=2, column=2, padx=5, pady=5)
    #     self.messageVar = StringVar()
    #     self.messageVar.set("")
    #     message = Label(messageFrame, textvariable=self.messageVar, width=60, height=3, wraplength=300)
    #     message.grid(row=1, column=1)
    #
    # def _initEditTools(self):
    #     """Sets up the edit tools frame and its parts, including buttons for clearing the maze, changing
    #     its numRows, changing modes (add walls, remove walls, place start, place goal), and loading and
    #     saving mazes from files"""
    #     self.editEnabled = True
    #     editFrame = Frame(self.root, bd=5, padx=5, pady=5, relief="groove")
    #     editFrame.grid(row=3, column=1, rowspan=2, padx=5, pady=5, sticky=N)
    #     editTitle = Label(editFrame, text="Edit Maze Options", font="Arial 16 bold", anchor=CENTER)
    #     editTitle.grid(row=0, column=1, padx=5, pady=5)
    #
    #     # Make a new maze subframe
    #     makerFrame = Frame(editFrame, bd=2, relief="groove", padx=5, pady=5)
    #     makerFrame.grid(row=1, column=1, padx=5, pady=5)
    #     makerLabel = Label(makerFrame, text="Create New Maze", font="Arial 14 bold", anchor=CENTER)
    #
    #     percLabel = Label(makerFrame, text="% Blocked")
    #     rowLabel = Label(makerFrame, text="# of Rows")
    #     colLabel = Label(makerFrame, text="# of Cols")
    #     self.userPerc = StringVar()
    #     self.userRows = StringVar()
    #     self.userCols = StringVar()
    #     self.userPerc.set(str(30))
    #     self.userRows.set(str(self.numRows))
    #     self.userCols.set(str(self.numCols))
    #     self.percEntry = Entry(makerFrame, textvariable=self.userPerc, width=4, justify=CENTER)
    #     self.rowsEntry = Entry(makerFrame, textvariable=self.userRows, width=4, justify=CENTER)
    #     self.colsEntry = Entry(makerFrame, textvariable=self.userCols, width=4, justify=CENTER)
    #
    #     self.flatButton = Button(makerFrame, text="New Maze", command=self.createFlat)
    #
    #     # place the basic buttons for editing frames
    #     makerLabel.grid(row=0, column=1, columnspan=4, padx=5)
    #     percLabel.grid(row=1, column=1)
    #     rowLabel.grid(row=1, column=3)
    #     colLabel.grid(row=2, column=3)
    #     self.percEntry.grid(row=2, column=1)
    #     self.rowsEntry.grid(row=1, column=4)
    #     self.colsEntry.grid(row=2, column=4)
    #
    #     self.flatButton.grid(row=3, column=1, columnspan=2, pady=5)
    #
    #     # Edit existing maze subframe
    #     editSubFrame = Frame(editFrame, bd=2, relief="groove", padx=5, pady=5)
    #     editSubFrame.grid(row=2, column=1, padx=5, pady=5)
    #
    #     editSubTitle = Label(editSubFrame, text="Edit Maze", font="Arial 14 bold", anchor=CENTER)
    #     editSubTitle.grid(row=0, column=1)  # , columnspan = 2)
    #     # Variables related to action settings
    #     self.editChoice = StringVar()
    #     self.editChoice.set("start")
    #
    #     # Create and place the radio buttons for maze editing
    #     self.addDelBlocks = Radiobutton(editSubFrame, variable=self.editChoice,
    #                                     text="Add/Del Blocks", value="addDelBlock", width=15, justify=LEFT)
    #     self.placeRobot = Radiobutton(editSubFrame, variable=self.editChoice,
    #                                   text="Move Robot", value="robot", width=15, justify=LEFT)
    #     self.addDelBlocks.grid(row=1, column=1)
    #     self.placeRobot.grid(row=3, column=1)
    #
    #     # Load and save maze subframe
    #     loadSaveFrame = Frame(editFrame, bd=2, relief="groove", padx=5, pady=5)
    #     loadSaveFrame.grid(row=3, column=1, padx=5, pady=5)
    #     loadSaveTitle = Label(loadSaveFrame, text="Load/Save Maze", font="Arial 14 bold", anchor=CENTER)
    #     loadSaveTitle.grid(row=0, column=1)  # , columnspan = 2)
    #
    #     self.loadButton = Button(loadSaveFrame, text="Load Maze", command=self.loadMaze)
    #     self.saveButton = Button(loadSaveFrame, text="Save Maze", command=self.saveMaze)
    #     self.loadButton.grid(row=1, column=1, pady=5)
    #     self.saveButton.grid(row=2, column=1, pady=5)
    #
    # def _initMazeGrid(self):
    #     """sets up the maze with given dimensions, done as a helper because it may need to be done over later"""
    #     self.canvas = None
    #     self.canvasSize = 500
    #     self.canvasPadding = 10
    #     canvasFrame = Frame(self.root, bd=5, padx=10, pady=10, relief="raise", bg="lemon chiffon")
    #     canvasFrame.grid(row=3, column=2, rowspan=2, padx=5, pady=5)
    #     self.canvas = Canvas(canvasFrame,
    #                          width=self.canvasSize + self.canvasPadding,
    #                          height=self.canvasSize + self.canvasPadding)
    #     self.canvas.grid(row=1, column=1)
    #     self.canvas.bind("<Button-1>", self.leftClickCallback)
    #     self.canvas.bind("<B1-Motion>", self.motionCallback)
    #     if self.blockPerc > 1.0:
    #         self.blockPerc = self.blockPerc / 100.0
    #     self.maze = MazeInfo('gen-flat', self.numRows, self.numCols, (0, 0), self.blockPerc)
    #
    #     self._createMazeGrid()
    #
    # # end _initMazeGrid
    #
    #
    # def _initLocalizeTools(self):
    #     """Sets up the localization control frame, with buttons for selecting which search, for starting a search,
    #     stepping or running it, and quitting from it.  You can also choose how many steps should happen
    #     for each click of the "step" button"""
    #     searchFrame = Frame(self.root, bd=5, padx=10, pady=10, relief="groove")
    #     searchFrame.grid(row=3, column=3, padx=5, pady=5, sticky=N)
    #     searchTitle = Label(searchFrame, text="MCL Control", font="Arial 16 bold")
    #     searchTitle.grid(row=0, column=1, padx=5, pady=5)
    #     self.searchType = StringVar()
    #     self.searchType.set("ucs")
    #
    #     sampleLabel = Label(searchFrame, text="Num Samples")
    #     self.userSampNum = StringVar()
    #     self.userSampNum.set(str(self.numSamples))
    #     self.sampEntry = Entry(searchFrame, textvariable=self.userSampNum, width=4, justify=CENTER)
    #
    #     self.initButton = Button(searchFrame, text="Set up MCL", command=self.setupMCL)
    #
    #     # place the basic buttons for editing frames
    #     sampleLabel.grid(row=0, column=1, padx=5, pady=5)
    #     self.sampEntry.grid(row=2, column=1, padx=5, pady=5)
    #     self.initButton.grid(row=3, column=1, padx=5, pady=5)
    #
    #     self.stepLoc = Button(searchFrame, text="Step MCL", command=self.stepMCL, state=DISABLED)
    #     self.runLoc = Button(searchFrame, text="Run MCL", command=self.runMCL, state=DISABLED)
    #     self.pauseLoc = Button(searchFrame, text="Pause MCL", command=self.pauseMCL, state=DISABLED)
    #     self.quitLoc = Button(searchFrame, text="Quit MCL", command=self.quitMCL, state=DISABLED)
    #     self.stepLoc.grid(row=15, column=1, padx=5, pady=5)
    #     self.runLoc.grid(row=16, column=1, padx=5, pady=5)
    #     self.pauseLoc.grid(row=17, column=1, padx=5, pady=5)
    #     self.quitLoc.grid(row=18, column=1, padx=5, pady=5)
    #
    # def _initLegend(self):
    #     """Sets up the legend that describes what each color means in the maze grid"""
    #     legendFrame = Frame(self.root, bd=5, padx=10, pady=10, relief="groove")
    #     legendFrame.grid(row=4, column=3, padx=5, pady=5, sticky=N)
    #     legend = Canvas(legendFrame, width=130, height=205)
    #     legend.grid(row=1, column=1)
    #     legendValues = {("light gray", "white", "Open space"),
    #                     ("dark cyan", "black", "Blocked"),
    #                     ("light gray", "green", "Start cell"),
    #                     ("light gray", "red", "Goal cell"),
    #                     ("magenta", "white", "Current cell"),
    #                     ("light pink", "white", "Explored cell"),
    #                     ("light blue", "white", "Fringe cell"),
    #                     ("yellow", 'white', "Shortest path")}
    #     row = 0
    #     col = 0
    #     for (cellColor, outlineCol, cellText) in legendValues:
    #         (x1, y1, x2, y2) = self._posToCoords(row, col)
    #         legend.create_rectangle(x1, y1, x2, y2, outline=outlineCol, fill=cellColor)
    #         legend.create_text(x1 + 25, y1 + 8, text=cellText, anchor=NW)
    #         row += 1
    #
    # # end _initLegend
    #
    #
    # ### =================================================================
    # ### Helper functions
    #
    #
    # def disableEdit(self):
    #     """Turn off access to the edit operations, by setting each of the GUI elements to DISABLED"""
    #     self.editEnabled = False
    #     self.flatButton.config(state=DISABLED)
    #     self.loadButton.config(state=DISABLED)
    #     self.saveButton.config(state=DISABLED)
    #     self.placeRobot.config(state=DISABLED)
    #     self.addDelBlocks.config(state=DISABLED)
    #     self.percEntry.config(state=DISABLED)
    #     self.rowsEntry.config(state=DISABLED)
    #     self.colsEntry.config(state=DISABLED)
    #
    # def enableEdit(self):
    #     """Turn on access to the edit operations, by setting each GUI element to NORMAL"""
    #     self.editEnabled = True
    #     self.flatButton.config(state=NORMAL)
    #     self.loadButton.config(state=NORMAL)
    #     self.saveButton.config(state=NORMAL)
    #     self.placeRobot.config(state=NORMAL)
    #     self.addDelBlocks.config(state=NORMAL)
    #     self.percEntry.config(state=NORMAL)
    #     self.rowsEntry.config(state=NORMAL)
    #     self.colsEntry.config(state=NORMAL)
    #
    # def disableMCL(self):
    #     """Turn off the search operations, by setting each GUI element to DISABLED."""
    #     # self.sampEntry.config(state=DISABLED)
    #     # self.initButton.config(state=DISABLED)
    #     self.stepLoc.config(state=DISABLED)
    #     self.pauseLoc.config(state=DISABLED)
    #     self.runLoc.config(state=DISABLED)
    #     self.quitLoc.config(state=DISABLED)
    #
    # def enableMCL(self):
    #     """Turn on the search operations, by setting each GUI element to NORMAL"""
    #     # self.sampEntry.config(state=NORMAL)
    #     # self.initButton.config(state=NORMAL)
    #     self.stepLoc.config(state=NORMAL)
    #     self.pauseLoc.config(state=NORMAL)
    #     self.runLoc.config(state=NORMAL)
    #     self.quitLoc.config(state=NORMAL)
    #
    # def _createMazeGrid(self):
    #     """This sets up the display of the maze, given the MazeInfo object.
    #     Re-called when dimensions changed."""
    #     self.squareToPos = {}
    #     self.posToSquare = {}
    #     self.posToText = {}
    #     startPos = self.maze.getRobotPos()
    #
    #     numRows = self.maze.getNumRows()
    #     numCols = self.maze.getNumCols()
    #     bigDim = max(numRows, numCols)
    #     if bigDim * 50 < self.canvasSize:
    #         self.cellSize = 50
    #     else:
    #         self.cellSize = self.canvasSize / bigDim
    #
    #     for row in range(numRows):
    #         for col in range(numCols):
    #             (x1, y1, x2, y2) = self._posToCoords(row, col)
    #             currId = self.canvas.create_rectangle(x1, y1, x2, y2)
    #             self.squareToPos[currId] = (row, col)
    #             self.posToSquare[row, col] = currId
    #             centerx = (x1 + x2) / 2
    #             centery = (y1 + y2) / 2
    #             textId = self.canvas.create_text(centerx, centery, text="0", font="arial 12")
    #             self.posToText[row, col] = textId
    #     self._displayMazeGrid()
    #
    # def _displayMazeGrid(self):
    #     """Set up a pristine view of the maze grid. Removes all sample data."""
    #     numRows = self.maze.getNumRows()
    #     numCols = self.maze.getNumCols()
    #     for row in range(numRows):
    #         for col in range(numCols):
    #             currId = self.posToSquare[row, col]
    #             (outlineColor, cellColor) = self._determineColor((row, col))
    #             self._setOutlineColor(currId, outlineColor)
    #             self._setCellColor(currId, cellColor)
    #             textId = self.posToText[row, col]
    #             self._setCellText(textId, '0')
    #
    # def _determineColor(self, currPos):
    #     (row, col) = currPos
    #     (sRow, sCol) = self.maze.getRobotPos()
    #     cellColor = "white"
    #     if row == sRow and col == sCol:
    #         outlineColor = 'blue'
    #         cellColor = "light blue"
    #     elif self.maze.isBlocked(row, col):
    #         outlineColor = 'black'
    #         cellColor = "dark gray"
    #     else:
    #         outlineColor = 'white'
    #         cellColor = "white"
    #     return (outlineColor, cellColor)
    #
    # ### =================================================================
    # ### The following are callbacks for the canvas itself
    # ### for the grid of rectangles
    #
    # def leftClickCallback(self, event):
    #     """This is a callback that happens when the user clicks in the maze part of the window.
    #     If edit is not enabled, then nothing happens.  If edit is enabled, then this finds the
    #     square that was clicked on, and changes its color.  Exactly how the color changes depends
    #     on a helper, and what color the grid square already was."""
    #
    #     if self.editEnabled:
    #         mouseX = event.x
    #         mouseY = event.y
    #         items = self.canvas.find_overlapping(mouseX - 2, mouseY - 2, mouseX + 2, mouseY + 2)
    #         print(items)
    #         if items == ():
    #             return
    #         # if len(items) > 2:
    #         #     print("Uh-oh, too many items")
    #
    #         sqItem = None
    #
    #         for item in items:
    #             if item in self.squareToPos:
    #                 sqItem = item
    #                 break
    #         if not sqItem:
    #             return
    #         (row, col) = self.squareToPos[sqItem]
    #         self._changeSquare(row, col, sqItem)
    #
    # def motionCallback(self, event):
    #     """This is a callback that happens when the user drags the mouse over the maze part.
    #     This finds the cell that corresponds to the location of the mouse, and changes its color.
    #     This allows the user to drag to create walls for the maze"""
    #     if self.editEnabled:
    #         (row, col) = self._coordToPos(event.x, event.y)
    #         item = self.posToSquare[row, col]
    #         self._changeSquare(row, col, item)
    #
    # def _changeSquare(self, row, col, item):
    #     """This function takes the row and column of an grid square item, and the item itself.
    #     It changes the color depending on what mode it is in.  The self.editChoice variable holds
    #     the mode the user has selected: black for adding walls, white for removing them, green for placing
    #     the start location, red for placing the goal.  This first handles the cases where the user
    #     is placing start or goal, because there can be only one start and goal location.  Thus, turning
    #     one grid cell green requires that we find the old green one (if any) and turn it white.  This calls a
    #     helper that actually does the color change"""
    #     currEdit = self.editChoice.get()
    #     if currEdit == "robot":
    #         (sRow, sCol) = self.maze.getRobotPos()
    #         startObj = self.posToSquare[sRow, sCol]
    #         self._setCellColor(startObj, "white")
    #         self._setOutlineColor(startObj, 'white')
    #         self.maze.setRobotPos((row, col))
    #     elif currEdit == "addDelBlock":  # if adding or blocks
    #         if self.maze.isBlocked(row, col):
    #             self.maze.delBlocked(row, col)
    #         else:
    #             self.maze.addBlocked(row, col)
    #     (outCol, cellCol) = self._determineColor((row, col))
    #     self._setCellColor(item, cellCol)
    #     self._setOutlineColor(item, outCol)
    #
    # ### =================================================================
    # ### The following are callbacks for buttons
    #
    # def showHelp(self):
    #     """Pop up a new window and display help information"""
    #     self.helpWindow = Toplevel()
    #     helpTxt = """Maybe someday..."""
    #
    #     textField = Label(self.helpWindow, text=helpTxt, padx=10, pady=10, justify=LEFT)
    #     closeButton = Button(self.helpWindow, text="Close", command=self.closeHelp)
    #     textField.grid(row=1, column=1)
    #     closeButton.grid(row=2, column=1)
    #
    # def closeHelp(self):
    #     """When the user closes the help window, destroy it"""
    #     self.helpWindow.destroy()
    #
    # def quit(self):
    #     """Callback for the quit button: destroy everything"""
    #     self.root.destroy()
    #
    # # ----------------------------------------------------------------
    # # Button callbacks for Edit buttons
    #
    #
    # def createFlat(self):
    #     """Creates a new flat maze of the given number of rows and columns. Note that this is a
    #     callback to the Create New Flat button, and it must first read the value of the StringVars
    #     to update the given size."""
    #     self._makeNewMaze('gen-flat')
    #
    # def _makeNewMaze(self, mode):
    #     self._removeMazeCells()
    #     userRowNum = self.userRows.get()
    #     userColNum = self.userCols.get()
    #     userPercNum = self.userPerc.get()
    #     try:
    #         self.numRows = int(userRowNum)
    #         self.numCols = int(userColNum)
    #         self.blockPerc = float(userPercNum)
    #     except:
    #         self._postMessage("# of Rows and # of Columns must be positive integers. % Blocked must be positive float.")
    #         return
    #     if self.blockPerc > 1.0:
    #         self.blockPerc = self.blockPerc / 100.0
    #     self.maze = MazeInfo(mode, self.numRows, self.numCols, (0, 0), self.blockPerc)
    #     self._createMazeGrid()
    #     self.currentSearch = None
    #
    # def _removeMazeCells(self):
    #     """A helper that removes all the grid cell objects from the maze, prior to creating new
    #     ones when the "Change Dimension" button is clicked"""
    #     for row in range(self.numRows):
    #         for col in range(self.numCols):
    #             currId = self.posToSquare[row, col]
    #             self.canvas.delete(currId)
    #     self.canvas.update()
    #     self.posToSquare = {}
    #     self.squareToPos = {}
    #
    # def loadMaze(self):
    #     """Callback for loading a maze. It uses a utility to ask the user to
    #     load a file. Then it clears the maze and resets it using the
    #     information from the file. The file contains text, first the
    #     numRows of the maze, and then that many lines. Each line contains
    #     words separated by spaces that describe the color for the
    #     corresponding cell. Thus there are numRows number of words per
    #     line."""
    #     fileName = tkFileDialog.askopenfilename(title="Select the file to load")
    #     if fileName != None:
    #         self.maze = MazeInfo('file', fileName)
    #         self._removeMazeCells()
    #         self.numRows = self.maze.getNumRows()
    #         self.numCols = self.maze.getNumCols()
    #         self._createMazeGrid()
    #         self.currentSearch = None
    #
    # def saveMaze(self):
    #     """This pops up a dialog box to save a maze to a file.  Note it won't save a maze with no
    #     start or goal.  It asks the MazeInfo object to write itself to this file."""
    #     fileName = tkFileDialog.asksaveasfilename(title="Select the file to which to save the current maze",
    #                                               initialfile="maze.txt")
    #     self.maze.writeGridToFile(fileName)
    #
    # # ----------------------------------------------------------------
    # # Button callbacks for Search buttons
    #
    #
    # def setupMCL(self):
    #     """Callback for initializing samples"""
    #     # clear any existing samples that may have been drawn
    #     self._displayMazeGrid()
    #     self.disableEdit()
    #     self.enableMCL()
    #
    #     sampVal = int(self.userSampNum.get())
    #     self.numSamples = sampVal
    #     print("Setup MCL", self.numSamples)
    #     self.localizer = MCL(self.maze, self.numSamples, self.numRows, self.numCols)
    #     currSamples = self.localizer.getSamples()
    #     self.markCells(currSamples)
    #
    # def runMCL(self):
    #     """This callback for the Run MCL button keeps running steps of the MCL algorithm until the search is done
    #     or a problem crops up.  """
    #     self.MCLIsRunning = True
    #
    # def pauseMCL(self):
    #     """This pauses the MCL process right where it is."""
    #     self.MCLIsRunning = False
    #
    # def stepMCL(self):
    #     """This performs one step of the MCL process, displaying the new positions."""
    #     currSamples = self.localizer.oneMCLStep()
    #     self._displayMazeGrid()
    #     self.markCells(currSamples)
    #
    # def quitMCL(self):
    #     """A callback for clearing away the search and returning to edit mode"""
    #     self.MCLIsRunning = False
    #     self._displayMazeGrid()
    #     self.disableMCL()
    #     self.enableEdit()
    #     self._clearMessage()
    #
    # def markCells(self, samples):
    #     """This function changes the color of grid cells to show the current samples."""
    #     sampleCounts = dict()
    #     # gather unique samples
    #     for s in samples:
    #         tupS = tuple(s)
    #         if tupS in sampleCounts:
    #             sampleCounts[tupS] += 1
    #         else:
    #             sampleCounts[tupS] = 1
    #
    #     for uniqSamp in sampleCounts:
    #         (sRow, sCol) = uniqSamp
    #         count = sampleCounts[uniqSamp]
    #         sqId = self.posToSquare[sRow, sCol]
    #         txId = self.posToText[sRow, sCol]
    #         self._setCellColor(sqId, "light green")
    #         self._setCellText(txId, str(count))
    #
    #     self.canvas.update()
    #
    # # -------------------------------------------------
    # # Utility functions
    #
    #
    # def _postMessage(self, messageText):
    #     """Posts a message in the message box"""
    #     self.messageVar.set(messageText)
    #
    # def _clearMessage(self):
    #     """Clears the message in the message box"""
    #     self.messageVar.set("")
    #
    # def _setCellColor(self, cellId, color):
    #     """Sets the grid cell with cellId, and at row and column position, to have the
    #     right color.  Note that in addition to the visible color, there is also a colors
    #     matrix that mirrors the displayed colors"""
    #     self.canvas.itemconfig(cellId, fill=color)
    #
    # def _setOutlineColor(self, cellId, color):
    #     """Sets the outline of the grid cell with cellID, and at row and column position, to
    #     have the right color."""
    #     self.canvas.itemconfig(cellId, outline=color)
    #
    # def _setCellText(self, textId, txt):
    #     """Sets the grid cell with cellId, and at row and column position, to have the
    #     right color.  Note that in addition to the visible color, there is also a colors
    #     matrix that mirrors the displayed colors"""
    #     self.canvas.itemconfig(textId, text=txt)
    #
    # def _posToId(self, row, col):
    #     """Given row and column indices, it looks up and returns the GUI id of the cell at that location"""
    #     return self.posToSquare[row, col]
    #
    # def _idToPos(self, currId):
    #     """Given the id of a cell, it looks up and returns the row and column position of that cell"""
    #     return self.squareToPos[currId]
    #
    # def _posToCoords(self, row, col):
    #     """Given a row and column position, this converts that into a position on the frame"""
    #     x1 = col * self.cellSize + 5
    #     y1 = row * self.cellSize + 5
    #     x2 = x1 + (self.cellSize - 2)
    #     y2 = y1 + (self.cellSize - 2)
    #     return (x1, y1, x2, y2)
    #
    # def _coordToPos(self, x, y):
    #     """Given a position in the frame, this converts it to the corresponding row and column"""
    #     col = (x - 5) / self.cellSize
    #     row = (y - 5) / self.cellSize
    #     if row < 0:
    #         row = 0
    #     elif row >= self.numRows:
    #         row = self.numRows - 1
    #
    #     if col < 0:
    #         col = 0
    #     elif col >= self.numRows:
    #         col = self.numRows - 1
    #
    #     return (int(row), int(col))

def RunKuri():
    """This starts it all up.  Sets up the KuriGUI, and its widgets, and makes it go"""
    k = KuriGUI()
    k.welcomeScreen()
    # s.setupWidgets()
    # s.goProgram()

# The lines below cause the maze to run when this file is double-clicked or sent to a launcher, or loaded
# into the interactive shell.
if __name__ == "__main__":
    RunKuri()
    mainloop()
