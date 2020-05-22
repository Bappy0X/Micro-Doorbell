from microbit import display, button_a, button_b, Image, accelerometer
import radio
from speech import say

radio.on()

#This code was used for a "messaging" system
"""while True:
    incoming = radio.receive()
    #display.show(Image.YES)
    display.scroll(incoming)
    say(incoming)"""

debounce = False
while True:
    if accelerometer.was_gesture("shake") or button_a.was_pressed() or button_b.was_pressed():
        if not debounce:
            radio.send("visitor")
            display.show(Image.YES)
            debounce = True
    sleep(10)