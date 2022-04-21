# macropad
Just a 6-key macropad but mine is better because RGB amirite

Archived as there are too many problems:
- Need a resister per RGB input, not one per output, as constant current across the RGBLED distorts the color otherwise. That's a lot of SMD components.
- The RPi Pico has a limited number of PWM units, not enough for running all of the RGBLEDs, and they were hooked up incorrectly anyway.
- Idea was ditched in favor of streamdekc instead.

# Materials
Parts used (Can easily be subbed for something similar):
- 1x [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- 1x [I2C OLED Display](https://www.adafruit.com/product/4440)
- 6x [Kailh Choc Switch](http://www.kailh.com/en/Products/Ks/CS/) (Linear or clicky with spring mechanism removed)
- 6x [Clear Kailh CHOC Keycaps](https://www.adafruit.com/product/5110)
- 6x [Diffused Rectangular RGB LEDs (5 x 2.5mm)](https://www.adafruit.com/product/2739) or something that fits in the Kailh holes
- MicroUSB cable
- 4x [M3-ish size plastic screws](https://www.amazon.com/dp/B00GDYDCC0) or similar
