# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
import pwmio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

# Setup PWM for LED
led = pwmio.PWMOut(board.GP15, frequency=5000, duty_cycle=65535)

button = DigitalInOut(board.GP16)
button.direction = Direction.INPUT
button.pull = Pull.UP

debounced_button = Debouncer(button)

kbd = Keyboard(usb_hid.devices)

button_fell = 0.0

def update_led(led, debounced_button):
    """Update the LED brightness based on the button state."""
    global button_fell
    if not debounced_button.value:
        led.duty_cycle = 0
    else:
        led.duty_cycle = min(int(65535 * (time.monotonic() - button_fell) / 0.5), 65535)    # fade out after half a second

while True:
    debounced_button.update()
    update_led(led, debounced_button)
    if debounced_button.fell:
        print("Button pressed!")
        kbd.press(Keycode.F13)
    if debounced_button.rose:
        print("Button released!")
        button_fell = time.monotonic()
        kbd.release(Keycode.F13)