import secrets
import pyperclip

AlphabetCap = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X", "Y", "Z"]
AlphabetLower = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"]
Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "'", ",", ".", "/", "?", "<", ">", "|", "[",
           "]", "{", "}", "`", "~"]
password = ""


def generatePassword(password):  # Function that generates the password, picking randomly from each array
    allLists = AlphabetCap + AlphabetLower + Symbols + Numbers
    password += "".join(secrets.choice(allLists))
    return password


while True:
    PassLength = int(input("Enter Password Length: "))  # Determines how long the password will be

    for x in range(PassLength):
        password = generatePassword(password)

    print(password)
    answer = input("Would you like to copy password to clipboard Y or N: ")
    if answer in ("Y", "y"):
        pyperclip.copy(password)  # Copies password to clipboard
        print(password, " Has been copied to clipboard")
    elif answer in ("N", "n"):
        answer = input("N to Exit or Y to regenerate password: ")
        if answer in ("N", "n"):
            print("Exit")
            break
        else:
            continue
