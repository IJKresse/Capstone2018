from gpiozero import InputDevice
import matplotlib.pyplot as plt

class HallSensor(object):
    samples = 100
    
    def __init__(self, inGPIO):
        self.voltage = InputDevice(inGPIO, True)
        
    def plotSamples(self);
        x = range(0, samples)
        for i in x:
            y[i] = self.voltage.value()
        
        plt.plot(x,y)

