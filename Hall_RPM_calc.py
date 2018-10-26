#I'm writing some code here that'll set up interrupts
#and calculate measured RPM. If you want to integrate
#it into the rest of the code, go ahead. It'll take me
#some time to figure out where it fits with OOD

#example, spin for 30 seconds
duration = 30

import RPi.GPIO as GPIO
import time
#set up for standard broadcom chip
GPIO.setmode(GPIO.BCM)

#hall sensor output feeds to GPIO17 right now, pull up
#to not conflict with pull up on sensor
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)


begin_revolution_time = time.time()

#wrapping in try except will ensure keyboard interrupts
#clean up GPIO pins, but it's a performance hit and I
#don't think it's really important
#try:
GPIO.wait_for_edge(17, GPIO.RISING)
last_rising_edge = time.time()
#except KeyboardInterrupt:
#    GPIO.cleanup()

while(time.time() < begin_revolution_time + duration):
    #try:
    GPIO.wait_for_edge(17, GPIO.RISING)
    new_rising_edge = time.time()
    spin_period = new_rising_edge - last_rising_edge
    last_rising_edge = new_rising_edge
    measured_rpm = 60/spin_period
    print(measured_rpm)
    #call other functions or whatever here
    
    #GPIO.cleanup()