import ev3dev.ev3 as ev3


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
    34 : "----.",       #9
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


inputTable = [".",".","-","-","-"]
inputString = ''.join(inputTable)
numOutput=[]
trueOutput=[]


def convertMorse():
    for count in range(0,len(morseDict)):
        if inputString == morseDict[count]:
            numOutput.append(count)
            print(numOutput)


def convertNumber():
    for count in range(0,len(numOutput)):
        trueOutput.append(letterDict[numOutput[count]])
        print(trueOutput)


for n in range(0,5):
    convertMorse()
    convertNumber()
    numOutput = []
    trueOutput = []
