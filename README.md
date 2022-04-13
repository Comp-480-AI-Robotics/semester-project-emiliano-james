# Kuri Robot Simulation
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
### Install the required packages
Make sure you have the compatible versions.
```
pip install -r requirements.txt 
```
### Run the program
```
python3 KuriProgram.py
```
## Contributors
[Anh Nguyen](https://github.com/theang66) <br>
[Lily Irvin](https://github.com/lirvin123) <br>
[Ryan Specht](https://github.com/rspecht) 
## Acknowledgements
Special thanks to Professor Susan Fox for her advice and support throughout this project!
