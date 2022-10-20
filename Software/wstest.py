from sqlite3 import Row
from turtle import delay
import board
import neopixel
import time
import random

NumOfLeds = 256
NumOfRows = 8
NumOfColumns = 32

DataPin = board.D18

pixels = neopixel.NeoPixel(DataPin, NumOfLeds)

while True:
    for i in range(NumOfLeds):
           R = random.randint(0, 255)
           G = random.randint(0, 255-R)
           B = random.randint(0, 255-G-R)
           pixels[i] = (R,G,B)
           time.sleep(0.010)
           pixels[i] = (0,0,0) 
       
    
   
