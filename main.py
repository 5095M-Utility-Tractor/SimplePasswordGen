import random
import secrets
import pyperclip

AlphabetCap = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X", "Y", "Z"]
AlphabetLower = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"]
Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "'", ",", ".", "/", "?", "<", ">", "|", "[", "]", "{", "}", "`", "~"]
password = ""


def generatePassword(password): # Function that generates the password, picking randomly from each array
    RandNum = random.randint(0, 3)
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


PassLength = int(input("Enter Password Length: ")) # Determines how long the password will be

for x in range(PassLength):
    password = generatePassword(password)

print(password)
answer = input("Would you like to copy password to clipboard Y or N: ")
if answer == "Y":
    pyperclip.copy(password) # Copies password to clipboard
    print(password, " Has been copied to clipboard")
elif answer == "N":
    print("Exit")

