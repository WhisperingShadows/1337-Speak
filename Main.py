subDict = {
        # "a": "4",
        # "i": "!",
        # "s": "$",
        "a": "@",
        "b": "8",
        "c": "(",
        "d": "|)",
        "e": "3",
        "g": "9",
        "i": "1",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7",
        "z": "2",
}

longSubDict = {
        "f": "|=",
        "h": "}{", # |-| ?
        "j": "_|",
        "k": "|<",
        "m": "|\/|",
        "n": "|\|",
        "p": "|>",
        "q": "<|",
        "r": "|^",
        "u": "|_|",
        "v": "\/",
        "w": "\/\/",
        "x": "><",
        "y": "`/",
}

SUB = True
LONG = True

##SUB = input("Use main simple substitution? Y/N: ")
##if SUB.lower() == "y":
##    SUB = True
##LONG = input("Use long-form substitution? Y/N: ")
##if LONG.lower() == "y":
##    LONG = True

text = list(input("Input the text to be modified: "))

if SUB:
    for char in range(len(text)):
        try:
            text[char] = subDict[text[char]]
        except:
            pass
if LONG:
    for char in range(len(text)):
        try:
            text[char] = longSubDict[text[char]]
        except:
            pass
        
print("Translated text:", "".join(text))
