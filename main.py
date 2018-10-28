from stepperMotor import StepperMotor
from DCMotor import DCMotor
from leadMotor import LeadMotor
from time import sleep
import RPi.GPIO as GPIO
from HallSensor import HallSensor

#Hall
Hall = HallSensor(17)

"""

# PCB
#Stepper
beakerMotor = StepperMotor(23,22,0.35)
beakerMotor.rotate_deg(120)

# Lead
zMotor = LeadMotor(15,14, 1.8)
zMotor.moveUpDown(100)
"""

# PCB
PCBMotor = DCMotor(27,3,4)
PCBMotor.spinAtSpeed()
sleep(2)
print(Hall.calcRPM())
##PCBMotor.changeSpeed(Hall.calcRPM(), 1000)
PCBMotor.speed = 0.1
PCBMotor.spinAtSpeed()
sleep(2)
print(Hall.calcRPM())
PCBMotor.stop()


#GPIO.cleanup()