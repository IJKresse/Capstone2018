from stepperMotor import StepperMotor
from DCMotor import DCMotor
from leadMotor import LeadMotor

beakerMotor = StepperMotor(15,14)
zMotor = leadMotor(27,22)
PCBMotor = DCMotor(2,3)

beakerMotor.rotate_deg(120)
zMotor.moveUpDown(10)
PCBMotor.spinAtSpeed()
PCBMotor.changeSpeed(200,150)
