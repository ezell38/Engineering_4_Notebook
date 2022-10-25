import board 

MORSE_CODE = { ' ':'/', 'A':'.-', 'B':'-...',     #Morse code dictionary
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}


while True:
    message = input("Enter Morse Code Message, or enter -q to quit: ")      #User input is now message
    
    
    if message == "-q":                   #If user inputs -q it quits the program
      break

    message = message.upper()             #Capatalizes message
    umym = ""                             #umym is now previous input

    for letter in message:                            #Run program on each individual character in message
      umym = umym + MORSE_CODE[letter] + " "          #Add new line to previous line and then add a space

    print(umym)