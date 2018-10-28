from stepperMotor import StepperMotor

class LeadMotor(StepperMotor):
    
    #STEPS_PER_REV = 200
    #STEPS_PER_DEG = STEPS_PER_REV/360
    NUM_BEAKERS = 5
    HEIGHT_PER_REV = 0.1
    #HEIGHT_PER_STEP = HEIGHT_PER_REV / STEPS_PER_REV
    #HEIGHT_PER_DEG = HEIGHT_PER_REV / STEPS_PER_DEG
    
    #def __init__(self):
    #    self.currentHeight = 0;
        
    def moveUpDown(self,dz):
        self.heightPerDeg = self.HEIGHT_PER_REV/self.stepsPerDeg
        numDeg = dz/self.heightPerDeg
        
        self.rotate_deg(numDeg)
        #self.currentHeight = self.currentHeight + dz
        
        
