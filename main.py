# Create 4 arrays Alphabet cap and lower case, Numbers and symbols Done
# Function that randomly picks an array then picks and adds it to password
import random
import secrets

from tkinter import Tk

AlphabetCap = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
AlphabetLower = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+"]
password = ""

def generatePassword(password):
    RandNum = random.randint(0,3)
    if RandNum == 0:
        item = secrets.choice(AlphabetCap)
        password += item
    elif RandNum == 1:
        item = secrets.choice(AlphabetLower)
        password += item
    elif RandNum == 2:
        item = secrets.choice(Numbers)
        password += item
    else:
        item = secrets.choice(Symbols)
        password += item
    return password

PassLength = int(input("Enter Password Length: "))

for x in range(PassLength):
   password = generatePassword(password)

print(password)
