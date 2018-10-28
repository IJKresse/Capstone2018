from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice
from time import sleep

class DCMotor(object):
    MAX_RPM = 3000
    
    def __init__(self, aGPIO, bGPIO, pwmGPIO):
        self.a = OutputDevice(aGPIO)
        self.b = OutputDevice(bGPIO)
        self.pwm = PWMOutputDevice(pwmGPIO,1000)
        self.speed = 0.9;
        self.rpm = 100;
        self.maxRPM = 5000
        
    def spinAtSpeed(self):
        self.a.on()
        self.b.off()
        self.pwm.on()
        self.pwm.value = self.speed

    def changeSpeed(self,Hall_rpm,desired_rpm):
        self.rpm = Hall_rpm;
        diff = ((Hall_rpm - desired_rpm)/MAX_RPM)
        spd = self.speed - diff
        self.speed = spd
        self.spinAtSpeed()       
    
    def stop(self):
        self.a.off()
        self.b.off()
        self.pwm.on()
        self.rpm = 0
        
    def dynamChangeSpeed(self, Hall, desiredRPM):
        while true:
            measuredRPM = Hall.calcRPM()
            self.changeSpeed(measuredRPM, desiredRPM)
            sleep(0.5)
        