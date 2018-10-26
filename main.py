from stepperMotor import StepperMotor
from DCMotor import DCMotor
from leadMotor import LeadMotor
from time import sleep

beakerMotor = StepperMotor(15,14)
zMotor = LeadMotor(27,22)
PCBMotor = DCMotor(2,3)

beakerMotor.rotate_deg(120)
zMotor.moveUpDown(10)
PCBMotor.spinAtSpeed()
sleep(5)
PCBMotor.changeSpeed(200,150)
sleep(5)
PCBMotor.stop()
