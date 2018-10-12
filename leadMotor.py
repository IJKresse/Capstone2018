from stepperMotor import StepperMotor

class LeadMotor(StepperMotor):
    HEIGHT_PER_REV = 10
    HEIGHT_PER_STEP = HEIGHT_PER_REV / STEPS_PER_REV
    HEIGHT_PER_DEG = HEIGHT_PER_REV / STEPS_PER_DEG
    
    def __init__(self):
        self.currentHeight = 0;
        
    def moveUpDown(self,dz):
        numDeg = dz/HEIGHT_PER_DEG
        
        self.rotate_deg(numDeg)
        self.currentHeight = self.currentHeight + dz
        
        