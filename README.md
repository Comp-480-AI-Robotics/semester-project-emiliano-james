# Kuri Robot Simulation
https://progress-bar.dev/<thepercentage>?title=< Kuri Functionality >
This project presents a simulation of the [Kuri robot](https://www.heykuri.com/explore-kuri/).
The Kuri robot will change its facial expression and heart light color depending on the sentiment of the text given by the 
user through chat or speech. We used [OpenCV](https://opencv.org/) to create the robot 
simulation, [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) to gather speech input, and 
[TextBlob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis.
## Chat Demo
[![Chat Demo](https://img.youtube.com/vi/5qmQ5Wap8Ts/0.jpg)](https://youtu.be/5qmQ5Wap8Ts)
## Speech Demo
[![Speech Demo](https://img.youtube.com/vi/frt1N9reglE/0.jpg)](https://youtu.be/frt1N9reglE)
## Getting started
This program requires Python 3. Below are step-by-step instructions for MacOS:
### Create a virtual environment
```
python3 -m venv venv 
source ./venv/bin/activate
```
## Installation

This Kuri robot requires [Python3](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg) 3.7+ to run.

```
pip install -r requirements.txt 
```
If you recieve an error as a result of portaudio, please enter the following command in your terminal
```
conda install pyaudio
```

```
### Run the program
```
python3 KuriProgram.py
```


## Contributors 
[Emiliano Huerta](https://github.com/EmilianoHuerta) <br>
[James Yang]() 

## Orignal Authors
[Anh Nguyen](https://github.com/theang66) <br>
[Lily Irvin](https://github.com/lirvin123) <br>
[Ryan Specht](https://github.com/rspecht) 


## Acknowledgements / Notes 
This repository was pre-exisiting from the authors above in which James and Emiliano have further built a social robot that mimics more to the orginal Kuri robot through the addition of the following: 
- More robust Speech Recognition
- Facial Recognition for its user 
- More responsive language features from Kuri