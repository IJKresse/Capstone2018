#from stepperMotor import StepperMotor
#from DCMotor import DCMotor
#from leadMotor import LeadMotor
#from time import sleep
import RPi.GPIO as GPIO
#from HallSensor import HallSensor
from Programs import Program
from time import sleep

prog = Program()
#prog.zMotor.moveUpDown(200)
prog.BeakerMotor.rotate_deg(200)
sleep(1)
#prog.PCBMotor.spinAtSpeed()
#prog.PCBMotor.stop()
#sleep(5)
#prog.PCBMotor.spinAtSpeed()
#prog.PCBMotor.speed = 1;
#prog.PCBMotor.dynamChangeSpeed(prog.Hall, 1000, 10)
#sleep(20)
#prog.prog1()

#GPIO.cleanup()
