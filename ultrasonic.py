import time
import RPi.GPIO as GPIO
import time

TRIG = 8
ECHO = 10
i = 0

dist_from_base = 10  # Write the distance from the sensor to the base of the bucket
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
print("Starting.....")
time.sleep(2)


def start():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_stop = time.time()

    pulse_time = pulse_stop - pulse_start
    distance = pulse_time * 17150
    distance = round(distance)

    return distance

        
        
        


