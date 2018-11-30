from gpiozero import OutputDevice
from time import sleep

class HDMIOutput(object):

    def __init__(self, switchGPIO):
        self.switch = OutputDevice(switchGPIO)

    def switchToMonitor(self):
        self.switch.on()

    def switchToProjector(self):
        self.switch.off()
