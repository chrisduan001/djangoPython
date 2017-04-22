import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def set_gpio_out(pin):
    GPIO.setwarnings(False)
    GPIO.setup(int(pin), GPIO.IN)
