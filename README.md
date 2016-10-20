# A very simple VU Meter to control your LEDs and Strips via Arduino !
The Python script uses the Tkinder Library to show a simple interface that lets you to play/pause the selected song "thesong.wav".
The script analyzes the spectrum and calculates some serial values to send via serial communication (port specified in the source code, a textbox will be implemented soon).

# Requirements
- Python 2/3 installed on an OSX / Linux / Windows OS
- Arduino IDE and Controller Drivers

# Setting everything up
- Edit the COM port and WAV Filename in the Script's source code.
- Edit the Arduino sketch in order to control your strips/LEDs , it depends on how you can turn them on/off with your controller : what you have to do is using the if/else and switch cases to manage the Serial Spectrum levels and turn on leds.

It's a very simple script. 
I hope it could be useful somehow, there will be some changes :)
