from gpiozero import OutputDevice
from time import sleep

class StepperMotor(object):
    
    STEPS_PER_REV = 200
    STEPS_PER_DEG = STEPS_PER_REV/360
    NUM_BEAKERS = 5

    def __init__(self,dirGPIO, pulseGPIO):
        self.dir = OutputDevice(dirGPIO)
        self.pulse = OutputDevice(pulseGPIO)
        self.currentAngle = 0;
        
    def rotate_deg(deg):
        numSteps = deg * STEPS_PER_DEG
    
        for i in range(0,numSteps):
            self.pulse.on()
            sleep(0.001)
            self.pulse.off()
            sleep(0.001)
            
        self.currentAngle = self.currentAngle + deg