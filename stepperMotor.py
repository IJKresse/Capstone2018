from gpiozero import OutputDevice
from time import sleep

class StepperMotor(object):
    NUM_BEAKERS = 5
    degPerPos = 360/NUM_BEAKERS

    def __init__(self,dirGPIO, pulseGPIO, stepSize):
        self.dir = OutputDevice(dirGPIO)
        self.pulse = OutputDevice(pulseGPIO)
        self.currentAngle = 0
        self.stepSize = stepSize
        self.stepsPerDeg = 1/stepSize
        
    def rotate_deg(self,deg):
        if(deg < 0):
            print("Move Down")
            self.dir.on()
        else:
            self.dir.off()
            
        numSteps = int(abs(deg) * self.stepsPerDeg)
        #print(self.stepsPerDeg)
        print(numSteps)
    
        for i in range(0,numSteps):
            self.pulse.on()
            sleep(0.001)
            self.pulse.off()
            sleep(0.001)
            
        self.currentAngle = self.currentAngle + deg
        
    def rotate_pos(self, numPos):
        deg = degPerPos * numPos
        self.rotate_deg(deg)
        
