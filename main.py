from microbit import display, button_a, button_b, sleep, Image
import radio, music

radio.on()

#This code was used for a "messaging" system
"""ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def selectChar():
    current = 0
    while True:
        A = button_a.was_pressed()
        B = button_b.was_pressed()
        display.show(ascii_uppercase[current])
        if A and B:
            return ascii_uppercase[current]
        elif A: #Go Backwards
            if current - 1 < 0:
                current = len(ascii_uppercase) - 1
            else:
                current -= 1
        elif B: #Go Forwards
            if current + 1 == len(ascii_uppercase):
                current = 0
            else:
                current += 1
        sleep(200)

def selectLength():
    current = 0
    while True:
        A = button_a.was_pressed()
        B = button_b.was_pressed()
        display.show(current)
        if A and B:
            return current
        elif A: #Go Backwards
            if current - 1 >= 0:
                current -= 1
        elif B: #Go Forwards
            current += 1
            #TODO: Add a maximum cap here
        sleep(200)

def selectString(length=3):
    theString = []
    for i in range(length):
        selectedChar = selectChar().upper()
        theString.append(selectedChar)
        display.show(Image.YES)
        sleep(200)
    theString.append(".")
    return ".".join(theString)

stringgg = selectString(length=selectLength())
radio.send(stringgg)
display.scroll("Sent")"""

active = False

while True:
    incoming = radio.receive()
    if incoming == "visitor":
        music.play(music.BA_DING)
        active = True
        a, b =(button_a.was_pressed(), button_b.was_pressed()) #This will reset was_pressed to false
        while active:
            if button_a.was_pressed() or button_b.was_pressed():
                active = False
                display.show(Image.YES)
                music.play(music.POWER_DOWN)
                sleep(1000)
                display.clear()
            else:
                for i in [Image("00000\n" "00000\n" "00900\n" "00000\n" "00000"), Image.SQUARE_SMALL, Image.SQUARE]:
                    display.show(i)
                    sleep(100)
    sleep(200)