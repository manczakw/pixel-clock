from sqlite3 import Row
from turtle import delay
import board
import neopixel
import time
import random
import sys
from datetime import datetime
 
 
# returns current date and time
now = datetime.now()
print("now = ", now)

NumOfLeds = 256
NumOfRows = 8
NumOfColumns = 32

DataPin = board.D18

pixels = neopixel.NeoPixel(DataPin, NumOfLeds)

LookUpTable = [[248,247,232,231,216,215,200,199,184,183,168,167,152,151,136,135,120,119,104,103,88,87,72,71,56,55,40,39,24,23,8,7],
[249,246,233,230,217,214,201,198,185,182,169,166,153,150,137,134,121,118,105,102,89,86,73,70,57,54,41,38,25,22,9,6],
[250,245,234,229,218,213,202,197,186,181,170,165,154,149,138,133,122,117,106,101,90,85,74,69,58,53,42,37,26,21,10,5],
[251,244,235,228,219,212,203,196,187,180,171,164,155,148,139,132,123,116,107,100,91,84,75,68,59,52,43,36,27,20,11,4],
[252,243,236,227,220,211,204,195,188,179,172,163,156,147,140,131,124,115,108,99,92,83,76,67,60,51,44,35,28,19,12,3],
[253,242,237,226,221,210,205,194,189,178,173,162,157,146,141,130,125,114,109,98,93,82,77,66,61,50,45,34,29,18,13,2],
[254,241,238,225,222,209,206,193,190,177,174,161,158,145,142,129,126,113,110,97,94,81,78,65,62,49,46,33,30,17,14,1],
[255,240,239,224,223,208,207,192,191,176,175,160,159,144,143,128,127,112,111,96,95,80,79,64,63,48,47,32,31,16,15,0]]

digits =[
   #0
  [[1,1,1],
   [1,0,1],
   [1,0,1],
   [1,0,1],
   [1,1,1]],
   #1
  [[0,0,1],
   [0,0,1],
   [0,0,1],
   [0,0,1],
   [0,0,1]],
   #2
  [[1,1,1],
   [0,0,1],
   [1,1,1],
   [1,0,0],
   [1,1,1]],
   #3
  [[1,1,1],
   [0,0,1],
   [1,1,1],
   [0,0,1],
   [1,1,1]],
   #4
  [[1,0,1],
   [1,0,1],
   [1,1,1],
   [0,0,1],
   [0,0,1]],
   #5
  [[1,1,1],
   [1,0,0],
   [1,1,1],
   [0,0,1],
   [1,1,1]],
   #6
  [[1,1,1],
   [1,0,0],
   [1,1,1],
   [1,0,1],
   [1,1,1]],
   #7
  [[1,1,1],
   [0,0,1],
   [0,0,1],
   [0,0,1],
   [0,0,1]],
   #8
  [[1,1,1],
   [1,0,1],
   [1,1,1],
   [1,0,1],
   [1,1,1]],
   #9
  [[1,1,1],
   [1,0,1],
   [1,1,1],
   [0,0,1],
   [1,1,1]],
   #none
  [[0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0]]
]

def setLedMatrix (row, column,value):
   pixels[LookUpTable[row][column]] = value

def setTime( hh,h,mm,m,colour):
   for vertical in range(-2,3):
      for horizontal in range(-1,2):

        r = digits[hh][vertical+2][horizontal+1] * colour[0]
        g = digits[hh][vertical+2][horizontal+1] * colour[1]
        b = digits[hh][vertical+2][horizontal+1] * colour[2]
     
        setLedMatrix (3+vertical, 7+horizontal,(r,g,b))

        r = digits[h][vertical+2][horizontal+1] * colour[0]
        g = digits[h][vertical+2][horizontal+1] * colour[1]
        b = digits[h][vertical+2][horizontal+1] * colour[2]
              
        setLedMatrix (3+vertical, 11+horizontal,(r,g,b))

             
        r = digits[mm][vertical+2][horizontal+1] * colour[0]
        g = digits[mm][vertical+2][horizontal+1] * colour[1]
        b = digits[mm][vertical+2][horizontal+1] * colour[2]
        setLedMatrix (3+vertical, 19+horizontal,(r,g,b))

       

        r = digits[m][vertical+2][horizontal+1] * colour[0]
        g = digits[m][vertical+2][horizontal+1] * colour[1]
        b = digits[m][vertical+2][horizontal+1] * colour[2]
     
        setLedMatrix (3+vertical, 23+horizontal,(r,g,b))

def updateCollon(second,colour):
   if(second%2 == 0):
      setLedMatrix(2,15,colour)
      setLedMatrix(4,15,colour)
   else:
      setLedMatrix(2,15,(0,0,0))
      setLedMatrix(4,15,(0,0,0))
 


while True:
 now = datetime.now()

 hh = now.hour//10
 h = now.hour%10
 mm = now.minute//10
 m = now.minute%10
 s = now.second
 
#-------------------------------------------

 if(now.hour <= 7):
   colour = (1,0,0)
 else:
   colour = (15,15,15)

 setTime(hh,h,mm,m,colour)
 updateCollon(s,colour)
 
 time.sleep(0.1)
