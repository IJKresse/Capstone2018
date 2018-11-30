from stepperMotor import StepperMotor
from DCMotor import DCMotor
from leadMotor import LeadMotor
from time import sleep
import RPi.GPIO as GPIO
from HallSensor import HallSensor

#Hall
Hall = HallSensor(17)
beakerMotor = StepperMotor(23,22,0.35)
zMotor = LeadMotor(15,14, 1.8)
PCBMotor = DCMotor(27,3,4)