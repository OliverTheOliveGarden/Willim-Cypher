#region Keybord Encode

QWERTYTranslation = {
    "q": "1",
    "w": "2",
    "e": "3",
    "r": "4",
    "t": "5",
    "y": "6",
    "u": "7",
    "i": "8",
    "o": "9",
    "p": "10",
    "a": "11",
    "s": "12",
    "d": "13",
    "f": "14",
    "g": "15",
    "h": "16",
    "j": "17",
    "k": "18",
    "l": "19",
    "z": "20",
    "x": "21",
    "c": "22",
    "v": "23",
    "b": "24",
    "n": "25",
    "m": "26",
    "Q": "1",
    "W": "2",
    "E": "3",
    "R": "4",
    "T": "5",
    "Y": "6",
    "U": "7",
    "I": "8",
    "O": "9",
    "P": "10",
    "A": "11",
    "S": "12",
    "D": "13",
    "F": "14",
    "G": "15",
    "H": "16",
    "J": "17",
    "K": "18",
    "L": "19",
    "Z": "20",
    "X": "21",
    "C": "22",
    "V": "23",
    "B": "24",
    "N": "25",
    "M": "26",
    " ": "-",
    ".": "/"
}
ABCTranslation = {
    "a":  "1",
    "b":  "2",
    "c":  "3",
    "d":  "4",
    "e":  "5",
    "f":  "6",
    "h":  "7",
    "g":  "8",
    "i":  "9",
    "j": "10",
    "k": "11",
    "l": "12",
    "m": "13",
    "n": "14",
    "o": "15",
    "p": "16",
    "q": "17",
    "r": "18",
    "s": "19",
    "t": "20",
    "u": "21",
    "v": "22",
    "w": "23",
    "x": "24",
    "y": "25",
    "z": "26",
    "A":  "1",
    "B":  "2",
    "C":  "3",
    "D":  "4",
    "E":  "5",
    "F":  "6",
    "G":  "7",
    "H":  "8",
    "I":  "9",
    "J": "10",
    "K": "11",
    "L": "12",
    "M": "13",
    "N": "14",
    "O": "15",
    "P": "16",
    "Q": "17",
    "R": "18",
    "S": "19",
    "T": "20",
    "U": "21",
    "V": "22",
    "W": "23",
    "X": "24",
    "Y": "25",
    "Z": "26",
    " ":  "-",
    ".":  "/"
}
DVORAKTranslation = {
    "p":  "1",
    "y":  "2",
    "f":  "3",
    "g":  "4",
    "c":  "5",
    "r":  "6",
    "l":  "7",
    "a":  "8",
    "o":  "9",
    "e": "10",
    "u": "11",
    "i": "12",
    "d": "13",
    "h": "14",
    "t": "15",
    "n": "16",
    "s": "17",
    "q": "18",
    "j": "19",
    "k": "20",
    "x": "21",
    "b": "22",
    "m": "23",
    "w": "24",
    "v": "25",
    "z": "26",
    "P":  "1",
    "Y":  "2",
    "F":  "3",
    "G":  "4",
    "C":  "5",
    "R":  "6",
    "L":  "7",
    "A":  "8",
    "O":  "9",
    "E": "10",
    "U": "11",
    "I": "12",
    "D": "13",
    "H": "14",
    "T": "15",
    "N": "16",
    "S": "17",
    "Q": "18",
    "J": "19",
    "K": "20",
    "X": "21",
    "B": "22",
    "M": "23",
    "W": "24",
    "V": "25",
    "Z": "26",
    " ":  "-",
    ".":  "/"
}

def getQWERTYtoNumber(input):
    output = ""
    for x in input:
        output += QWERTYTranslation[x] + "."
    return output

def getABCtoNumber(input):
    output = ""
    for x in input:
        output += ABCTranslation[x] + "."
    return output

def getDVORAKtoNumber(input):
    output = ""
    for x in input:
        output += DVORAKTranslation[x] + "."
    return output

#endregion
#region Run Funcs

def askChoices(choices, qustion):
    askString = ""
    i = 1
    for x in choices:
        askString += str(i) + ". " + x + " "
        i += 1
    i = 0
    askString += "\n"
    print(qustion)
    return input(askString)

def runKeybord():

    a = askChoices(("QWERTY", "ABC", "DVORAK"), "Pick Keyboard")
    if (a == "1"):
        print(getQWERTYtoNumber(input("Enter String \n")))
    elif (a == "2"):
        print(getABCtoNumber(input("Enter String \n")))
    elif (a == "3"):
        print(getDVORAKtoNumber(input("Enter String \n")))
    else:
        print("INVALID INPUT")
        runKeybord()

def runCypher():
    a = askChoices(("KeyBoard", "1"), "Pick Cypher Type")
    if (a == "1"):
       runKeybord()
    elif (a == "END"):
        return
    else:
        print("INVALID INPUT")
        runCypher()
    print("\n")
    runCypher()

#endregion
print("Type \"END\" to stop program")
runCypher()