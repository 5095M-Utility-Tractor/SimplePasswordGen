import PySimpleGUI as SG
import secrets

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

layout = [[SG.Text("Input Password Length")], [SG.InputText(key='-INPUT-')], [SG.Button("Generate")], [SG.Text(password, key='-PASSWORD-')]]
window = SG.Window("PassGen", layout)


def generatePassword(password):  # Function that generates the password, picking randomly from each array
    allLists = AlphabetCap + AlphabetLower + Symbols + Numbers
    for x in range(PassLength):  # Pick a Random Character for Length of Password
        password += "".join(secrets.choice(allLists))
    return password


while True:
    event, values = window.read()
    if event == SG.WIN_CLOSED:
        break
    elif event == "Generate":
        PassLength = int(values['-INPUT-'])
        password = generatePassword(password)
        window['-PASSWORD-'].update(password)
        continue
    window.close()
