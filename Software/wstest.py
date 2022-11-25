from sqlite3 import Row
from turtle import delay
import board
import neopixel
import time
import random
import sys

NumOfLeds = 256
NumOfRows = 8
NumOfColumns = 32

DataPin = board.D18

pixels = neopixel.NeoPixel(DataPin, NumOfLeds)

def OneHot():
    for i in range(NumOfLeds):
           R = random.randint(0, 255)
           G = random.randint(0, 255-R)
           B = random.randint(0, 255-G-R)
           pixels[i] = (R,G,B)
           time.sleep(0.010)
           pixels[i] = (0,0,0) 

def TwoRows():
    for i in range(16):
        R = random.randint(0, 255)
        G = random.randint(0, 255-R)
        B = random.randint(0, 255-G-R)
        pixels[i] = (R,G,B)
    time.sleep(5)
    for i in range(16):
        pixels[i] = (0,0,0)
    time.sleep(5)

def FourRows():
    for i in range(256):
        R = random.randint(0, 10)
        G = random.randint(0, 10-R)
        B = random.randint(0, 10-G-R)
        pixels[i] = (R,G,B)
    time.sleep(5)
    for i in range(256):
        pixels[i] = (0,0,0)
    time.sleep(5)

def six():
    
       
        pixels[2] = (125,125,125)
        pixels[3] = (125,125,125)
        pixels[4] = (125,125,125)
        pixels[13] = (125,125,125)
        pixels[18] = (125,125,125)
        pixels[19] = (125,125,125)
        pixels[20] = (125,125,125)
        pixels[11] = (125,125,125)
        pixels[21] = (125,125,125)
        pixels[22] = (125,125,125)
        pixels[9] = (125,125,125)
        pixels[6] = (125,125,125)

def BlackDown():
    for i in range(NumOfLeds):  
        pixels[i] = (0,0,0) 

while True:
    OneHot()
    #FourRows()
    #pixels[0] = (255,255,255)
    #pixels[12] = (255,255,255)
    #six()








            
          
       
    
   

