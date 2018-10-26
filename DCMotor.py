from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice
from time import sleep

class DCMotor(object):
    
    def __init__(self, enGPIO, pwmGPIO):
        self.en = OutputDevice(enGPIO)
        self.pwm = PWMOutputDevice(pwmGPIO,1000)
        self.speed = 1.0;
        self.rpm = 100;
        
    def spinAtSpeed(self):
        self.en.on()
        self.pwm.on()
        self.pwm.value = self.speed

    def changeSpeed(self,Hall_rpm,desired_rpm):
        self.rpm = Hall_rpm;
        spd = ((desired_rpm - Hall_rpm)/desired_rpm)+self.speed
        self.speed = spd
        self.spinAtSpeed()       
    
    def stop(self):
        self.en.off()
        self.pwm.off()
        self.speed = 0
        self.rpm = 0
        