import RPi.GPIO as GPIO
import time

# GPIO ports for the LEDs
LedPins = [17, 27, 22, 23, 24, 25, 16, 26]

def stop_code():
    print("Press Ctrl+C to end the program.")

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPins, GPIO.OUT, initial=GPIO.LOW)

def main():
    print_message()

    while True:
        for i in range(8):
            GPIO.output(LedPins[i], GPIO.HIGH)
            GPIO.output(LedPins[-(i+1)], GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LedPins[i], GPIO.LOW)
            GPIO.output(LedPins[-(i+1)], GPIO.LOW)

def cleanup():
    GPIO.output(LedPins, GPIO.HIGH)
    GPIO.cleanup()

def print_message():
    print("Starting the LED sequence.")

if __name__=="__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
