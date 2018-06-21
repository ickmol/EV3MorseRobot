#!/usr/bin/env python3
from ev3dev.ev3 import *
from timeit import default_timer as timer


# Initialising Variables
inputAllowed = True
programActive = True

morseDict = {0: ".-",   #A
    1: "-...",          #B
    2: "-.-.",          #C
    3: "-..",           #D
    4: ".",             #E
    5: "..-.",          #F
    6: "--.",           #G
    7: "....",          #H
    8: "..",            #I
    9: ".---",          #J
    10: "-.-",          #K
    11: ".-..",         #L
    12: "--",           #M
    13: "-.",           #N
    14: "---",          #O
    15: ".--.",         #P
    16: "--.-",         #Q
    17: ".-.",          #R
    18: "...",          #S
    19: "-",            #T
    20: "..-",          #U
    21: "...-",         #V
    22: ".--",          #W
    23: "-..-",         #X
    24: "-.--",         #Y
    25: "--..",         #Z

    #Numbers Start
    26 : ".----",       #1
    27 : "..---",       #2
    28 : "...--",       #3
    29 : "....-",       #4
    30 : ".....",       #5
    31 : "-....",       #6
    32 : "--...",       #7
    33 : "---..",       #8
    34 : "----.",		#9
    35 : "-----"        #0
    }


letterDict = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",
    26: "1",
    27: "2",
    28: "3",
    29: "4",
    30: "5",
    31: "6",
    32: "7",
    33: "8",
    34: "9",
    35: "0"
    }


# Initialise Other Processes


def touchInput():           # Defines a function which can be called upon in the main code at any time
    StartTime = timer()     # Log a time within system clock as a value, the is considered the "Last Pressed" time
    EndTime = timer() + 3
    inputTable = []  # inputs initially put into a table for easier communication with ev3 sensors
    global inputString

    ts1 = TouchSensor('in2')
    ts2 = TouchSensor('in3')

    print('Please Input Now')

    while EndTime + 5 > StartTime:              # loops until  the time between a switch was last pressed and idle > 5 seconds
        if ts1.is_pressed:                      # Check for left touch sensor input for dot (.) morse inputs
                inputTable.append(".")          # Add a dot input to an input table to be later converted
                StartTime = timer()             # Restart the clock since the timer was last reset
                print('.')
                time.sleep(0.5)
                print('wait...')

        if ts2.is_pressed:                  # Check for right touch sensor input for dash (-) morse inputs
                inputTable.append("-")          # add a dash input to an input table to be later converted
                StartTime = timer()             # Restart the clock since the timer was last reset
                print("-")
                time.sleep(0.5)
                print('wait...')

        else:                                   # When neither touch sensor receives an input:
                EndTime = timer()               # Run a continuous timer until the 'input' phase is terminated

    print('Ending Input... Please Wait!')
    inputString = str(inputTable)



#Converts Morse code into number code (morseDict)
def convertMorse():
    for count in range(0,len(morseDict)):
        if inputString == morseDict[count]:
            numOutput.append(count)
            print(numOutput)


#Converts number code to letters (letterDict)
def convertNumber():
    for count in range(0, len(numOutput)):					#Loops the conversion from number to letter so that it can handle conversions of multiple numbers at once
        trueOutput.append(letterDict[numOutput[count]])		#Adds the letter to the trueOutput table

def displayOutput():
    print(inputString)
    print(trueOutput)


while programActive:
    touchInput()
    convertMorse()
    convertNumber()
    displayOutput()
    numOutput = []
    trueOutput = []