import RPi.GPIO as GPIO
import time

# GPIO ports for the LEDs
led_ports = [17, 27, 22, 23, 24, 25, 16, 26]

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up LED ports as output
for port in led_ports:
    GPIO.setup(port, GPIO.OUT)

# Function to blink one LED
def blink_led(port, duration):
    GPIO.output(port, GPIO.HIGH)   # Turn on the LED
    time.sleep(duration)           # Wait for the specified duration
    GPIO.output(port, GPIO.LOW)    # Turn off the LED

# Function to shift back and forth among LEDs
def shift_leds(duration):
    for port in led_ports:
        GPIO.output(port, GPIO.HIGH)   # Turn on the LED
        time.sleep(duration)           # Wait for the specified duration
        GPIO.output(port, GPIO.LOW)    # Turn off the LED
		
		# Reverse the list of LED ports and repeat the process
    for port in reversed(led_ports):
        GPIO.output(port, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(port, GPIO.LOW)

try:
    while True:
        # Blink one LED
        blink_led(led_ports[0], 1)

        # Shift among LEDs
        shift_leds(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
