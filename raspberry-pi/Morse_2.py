import board 
import time 
import digitalio  

led=digitalio.DigitalInOut(board.GP18)


led.direction=digitalio.Direction.OUTPUT


MORSE_CODE = { ' ':'/', 'A':'.-', 'B':'-...',
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

modifier = 0.25
dot_time = 1*modifier         
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier


while True:
    message = input("Enter Morse Code Message, or enter -q to quit: ")
    
    
    if message == "-q":
      break

    message = message.upper()
    umym = ""

    for letter in message:
      umym = umym + MORSE_CODE[letter] + " "

    print(umym)

    for character in umym:
      if character == ".":            #If the character is a "." turn on the led for dot time
        led.value=True
        time.sleep(dot_time)
        led.value=False
        time.sleep(between_taps)


      if character == "-":          #If the character is a "-" turn on the led for dash time
        led.value=True
        time.sleep(dash_time)
        led.value=False
        time.sleep(between_taps)

      if character == " ":        #If the character is a space sleep for the allotted amount of time 
        time.sleep(between_words)
