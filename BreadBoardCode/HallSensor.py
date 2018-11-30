import RPi.GPIO as GPIO
import time

class HallSensor(object):
    samples = 100
    
    def __init__(self, inGPIO):
        self.inPin = inGPIO
        self.SampleLength = 10
        self.sampleRPM = []
        #set up for standard broadcom chip
        GPIO.setmode(GPIO.BCM)
        self.pull_up_down = GPIO.PUD_UP

        #hall sensor output feeds to GPIO17 right now, pull up
        #to not conflict with pull up on sensor
        GPIO.setup(self.inPin, GPIO.IN, self.pull_up_down)
        
        
    
    def calcRPM(self):
        
        begin_revolution_time = time.time()
        self.sampleRPM = []

        #clean up GPIO pins, but it's a performance hit and I
        #don't think it's really important
        #try:
        GPIO.wait_for_edge(self.inPin, GPIO.RISING)
        last_rising_edge = time.time()
        #except KeyboardInterrupt:
        #    GPIO.cleanup()

        while(time.time() < begin_revolution_time + self.SampleLength):
            #try:
            GPIO.wait_for_edge(self.inPin, GPIO.RISING)
            new_rising_edge = time.time()
            spin_period = new_rising_edge - last_rising_edge
            last_rising_edge = new_rising_edge # Merge conflict in head
            measured_rpm = 60/spin_period
            return measured_rpm
            #call other functions or whatever here
    
            #GPIO.cleanup()

    def wait_til_aligned(self):
            GPIO.wait_for_edge(self.inPin, GPIO.RISING)
            
