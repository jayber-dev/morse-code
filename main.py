from ntpath import join
import winsound
from numpy import append
import time


morse_data = {
    'A': '.-' ,
    'B': '-..',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    }



user_input = input('enter text \n').upper()

# print(user_input)
morse_string = ""
for i in user_input:
    if i in morse_data:
        to_add = morse_data[i]
        morse_string = morse_string + " " + morse_data[i]

print(morse_string)

for i in morse_string:
    print(i)
    if i == ".":
        winsound.Beep(1500,200)     
        time.sleep(0.1)
    elif i == "-":
        winsound.Beep(1500,500)
        time.sleep(0.1)
    else:
        time.sleep(0.4)


print(morse_string)