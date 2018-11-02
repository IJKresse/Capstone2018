from DCMotor import DCMotor
from HallSensor import HallSensor

#basically the flow should be
# 1. spin at 1000RPM or whatever to spin coat
# 2. either let it coast or brake then dynamChangeSpeed,
#        or skip straight to dynamChangeSpeed to get slow rotation
# 3. Once dynamChangeSpeed finishes and the board is spinning slowly
#        

#set up the hall sensor class for later
Hall = HallSensor(17)

#If I'm understanding correctly, this spends 15 seconds tuning
#speed to get the motor running at 12 RPM
PCBMotor = DCMotor(27,3,4)
PCBMotor.dynamChangeSpeed(Hall, 12)

#on the next rising edge, immediately brake
GPIO.wait_for_edge(self.inPin, GPIO.RISING)
PCBMotor.stop()
#looks like stop() uses the current value of speed for the braking PWM
#I'd like to have it brake at at 100% PWM to stop it as quickly as possible
#at least in this case. Generally, the faster the rotational speed
#the lower the braking pwm value should be. Probably should be mod.ified in DCMotor.py