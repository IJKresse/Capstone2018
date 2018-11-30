from HallSensor import HallSensor
from DCMotor import DCMotor
from stepperMotor import StepperMotor
from leadMotor import LeadMotor
from time import sleep
from ImageDisplay import Display


class Program(object):

    def __init__(self):
        self.Hall = HallSensor(17)
        self.BeakerMotor = StepperMotor(23,22,0.35)
        self.zMotor = LeadMotor(18,14,1.8)
        self.PCBMotor = DCMotor(27,3,4)


    def align(self):
        self.PCBMotor.dynamChangeSpeed(self.Hall,300,5)
        self.Hall.wait_til_aligned()
        self.PCBMotor.stopQuickly()

    def spinCoatExpose(self):
        #Dip into beaker
        self.zMotor.moveUpDown(-500)
        sleep(1)
        # Mix Photopolymer
        self.PCBMotor.spinAtSpeed()
        self.PCBMotor.dynamChangeSpeed(self.Hall, 300, 10)
        self.PCBMotor.stop()
        sleep(1)
        # Remove from photopolymer
        self.zMotor.moveUpDown(250)

        # Spin to thin layer and align
        self.PCBMotor.spinAtSpeed()
        self.PCBMotor.dynamChangeSpeed(self.Hall, 1000, 30)
        self.align()

        # Project image
        d = Display("binaryMask.png", 5)

        # Remove from beaker
        self.zMotor.moveUpDown(250)

    def dipNmix(self,duration):
        self.zMotor.moveUpDown(-500)
        sleep(0.5)
        # Mix Solution
        self.PCBMotor.spinAtSpeed()
        self.PCBMotor.dynamChangeSpeed(self.Hall, 100, 10)
        self.PCBMotor.stop()
        sleep(0.5)
        self.zMotor.moveUpDown(500)

    def prog1(self):
        # Photopolymer
        self.spinCoatExpose()

        # Wash w/ IPA
        #self.BeakerMotor.rotate_pos(1)
        #self.dipNMix(20)

        # Etch in acid
        #self.BeakerMotor.rotate_pos(1)
        #self.dipNMix(20)
        

        
        
        
        
