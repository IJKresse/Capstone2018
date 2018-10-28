from gpiozero import OutputDevice
from time import sleep

class StepperMotor(object):
    NUM_BEAKERS = 5

    def __init__(self,dirGPIO, pulseGPIO, stepSize):
        self.dir = OutputDevice(dirGPIO)
        self.pulse = OutputDevice(pulseGPIO)
        self.currentAngle = 0
        self.stepSize = stepSize
        self.stepsPerDeg = 1/stepSize
        
    def rotate_deg(self,deg):
        numSteps = int(deg * self.stepsPerDeg)
        print(self.stepsPerDeg)
        print(numSteps)
    
        for i in range(0,numSteps):
            self.pulse.on()
            sleep(0.001)
            self.pulse.off()
            sleep(0.001)
            
        self.currentAngle = self.currentAngle + deg
