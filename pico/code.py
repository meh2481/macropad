import time
import board
import pwmio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

# Setup PWM for LEDs
leds_r = [
    pwmio.PWMOut(board.GP1), #frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP5), #, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP9), #, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP13), #, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP19), #, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP26), #, frequency=5000, duty_cycle=65535)
]

leds_g = [
    pwmio.PWMOut(board.GP2), #, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP6), #, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP10), #, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP14, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP20, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP27, frequency=5000, duty_cycle=65535)
]

leds_b = [
    None, # pwmio.PWMOut(board.GP3, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP7, frequency=5000, duty_cycle=65535),
    None, # pwmio.PWMOut(board.GP11, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP15, frequency=5000, duty_cycle=65535),
    None, # pwmio.PWMOut(board.GP21, frequency=5000, duty_cycle=65535),
    pwmio.PWMOut(board.GP28, frequency=5000, duty_cycle=65535)
]

buttons = [
    DigitalInOut(board.GP0),
    DigitalInOut(board.GP4),
    DigitalInOut(board.GP8),
    DigitalInOut(board.GP12),
    DigitalInOut(board.GP18),
    DigitalInOut(board.GP22)
]

for button in buttons: 
    button.direction = Direction.INPUT
    button.pull = Pull.UP

debounced_buttons = [Debouncer(button) for button in buttons]

kbd = Keyboard(usb_hid.devices)

button_rose_times = [0.0] * len(buttons)

keycodes = [
    Keycode.F13,
    Keycode.F14,
    Keycode.F15,
    Keycode.F16,
    Keycode.F17,
    Keycode.F18
]

def update_led(led, debounced_button, button_rose_time):
    """Update the LED brightness based on the button state."""
    if not led:
        return
    if not debounced_button.value:
        led.duty_cycle = 0
    else:
        time_diff = time.monotonic() - button_rose_time
        if time_diff > 0.75:
            return # Skip updating PWM to prevent flicker
        led.duty_cycle = min(int(65535 * (time_diff / 0.5)), 65535)    # fade out after half a second

while True:
    # Update the debounced button states
    for debounced_button in debounced_buttons:
        debounced_button.update()
    
    # Update LEDs
    for i in range(len(buttons)):
        # For now just fade out blue
        update_led(leds_r[i], debounced_buttons[i], button_rose_times[i])

        # Check for button presses
        if debounced_buttons[i].fell:
            kbd.press(keycodes[i])
        # Check for button releases
        if debounced_buttons[i].rose:
            button_rose_times[i] = time.monotonic()
            kbd.release(keycodes[i])