import RPi.GPIO as GPIO
import time

# GPIO ports for the LEDs
led_pins = [17, 27, 22, 23, 24, 25, 16, 26]

# Set up LED ports as output
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)

# Blink LEDs in different directions
def blink_leds():
    for i in range(2):
        for j in range(4):
            # Blink center LEDs
            GPIO.output(led_pins[3 - j], GPIO.HIGH)
            GPIO.output(led_pins[4 + j], GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led_pins[3 - j], GPIO.LOW)
            GPIO.output(led_pins[4 + j], GPIO.LOW)
            time.sleep(0.2)

        for j in range(4):
            # Blink outer LEDs
            GPIO.output(led_pins[4 + j], GPIO.HIGH)
            GPIO.output(led_pins[3 - j], GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led_pins[4 + j], GPIO.LOW)
            GPIO.output(led_pins[3 - j], GPIO.LOW)
            time.sleep(0.2)

# Move LEDs back to center
def move_back_leds():
    for i in range(3):
        for j in range(4):
            GPIO.output(led_pins[3 - j], GPIO.HIGH)
            GPIO.output(led_pins[4 + j], GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led_pins[3 - j], GPIO.LOW)
            GPIO.output(led_pins[4 + j], GPIO.LOW)
            time.sleep(0.2)
    
    GPIO.cleanup()

try:
    blink_leds()
    move_back_leds()

except KeyboardInterrupt:
    GPIO.cleanup()
