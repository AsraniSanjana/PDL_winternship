import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_pin=7

GPIO.setup(LED_pin, GPIO.OUT)

while 1:
   GPIO.output(LED_pin,True)
   time.sleep(1)
