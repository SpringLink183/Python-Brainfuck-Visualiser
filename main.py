# >+++++++++++++++
# ++++++++++++++++
# ++++++++++++++++
# ++++++++++++++++
# +++++++++++++++.
# ++++++++++++++++
# +++.++++++++++++
# ++.--.----.>++++
# ++++++++++++++++
# ++++++++++++.<++
# ++++++++++++.---
# ----------------
# ---.++++++++++++
# ++++++.>.<------
# -----.---.++++++
# +++++++.--------
# -----.>.>+++.
# [[-]<]+[]

import hexNumIn as bfRes
import tkinter as tk
from tkinter import filedialog
import ctypes
import time
import sys
import os

os.system("cls")

if (len(sys.argv) == 2):
    ctypes.windll.kernel32.SetConsoleTitleW("Loading Program...")
    f = open(sys.argv[1], "r")
    rawProgramData = f.read()
    f.close()
else:
    ctypes.windll.kernel32.SetConsoleTitleW("Requesting Brainfuck Program")
    print("Please select brainfuck program to run..")
    fileLocation = filedialog.askopenfilename()
    if (fileLocation == ""):
        print("No File Selected..")
        time.sleep(3)
        exit()
    ctypes.windll.kernel32.SetConsoleTitleW("Loading Program...")
    f = open(fileLocation, "r")
    rawProgramData = f.read()
    f.close()


i = 0
o = len(rawProgramData) - 1
finalProgramData = ""

while (i <= o):
    if (rawProgramData[i] == "+"):
        finalProgramData+="+"
    if (rawProgramData[i] == "-"):
        finalProgramData+="-"
    if (rawProgramData[i] == ">"):
        finalProgramData+=">"
    if (rawProgramData[i] == "<"):
        finalProgramData+="<"
    if (rawProgramData[i] == ","):
        finalProgramData+=","
    if (rawProgramData[i] == "."):
        finalProgramData+="."
    if (rawProgramData[i] == "["):
        finalProgramData+="["
    if (rawProgramData[i] == "]"):
        finalProgramData+="]"
    i+=1

cell = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
cell[0] = 0
cell[1] = 0
cell[2] = 0
cell[3] = 0
cell[4] = 0
cell[5] = 0
cell[6] = 0
cell[7] = 0
cell[8] = 0
cell[9] = 0
cell[10] = 0
cell[11] = 0
cell[12] = 0
cell[13] = 0
cell[14] = 0
cell[15] = 0
currentCell = 0

i = 0
o = len(finalProgramData) - 1
bfOutput = ""
output = bfRes.textP(cell[currentCell])
errors = 0
save = {}
backTracks = 0

ctypes.windll.kernel32.SetConsoleTitleW("Running..")

while (i <= o):
    os.system("cls")
    if (finalProgramData[i] == "+"):
        if (cell[currentCell] >= 255):
            cell[currentCell] = 0
        else:
            cell[currentCell]+=1
    
    if (finalProgramData[i] == "-"):
        if (cell[currentCell] <= 0):
            cell[currentCell] = 255
        else:
            cell[currentCell]-=1
    
    if (finalProgramData[i] == ">"):
        if (currentCell >= 15):
            errors+=1
        else:
            currentCell+=1
    
    if (finalProgramData[i] == "<"):
        if (currentCell <= 0):
            errors+=1
        else:
            currentCell-=1
    
    if (finalProgramData[i] == ","):
        print("incomplete feature..")
    
    if (finalProgramData[i] == "."):
        output = bfRes.textP(cell[currentCell])
    
    if (finalProgramData[i] == "["):
        if (cell[currentCell] == 0):
            nul = 0
        else:
            backTracks += 1
            save[backTracks] = i
    
    if (finalProgramData[i] == "]"):
        if (cell[currentCell] == 0):
            backTracks -= 1
        else:
            i = save[backTracks]
    
    bfOutput += output[1]
    output[1] = ""
    
    print("Output: " + bfOutput + "\nCells: " + str(cell) + "\nPoint: " + str(currentCell) + "   Errors: " + str(errors) + "   Current Part: " + str(finalProgramData[i]) + "\nBackTracks: " + str(save))
    time.sleep(0.0)
    i+=1

ctypes.windll.kernel32.SetConsoleTitleW("Done..")
os.system("pause")