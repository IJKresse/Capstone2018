from gpiozero import OutputDevice
from time import sleep

STEPS_PER_REV = 200
STEPS_PER_DEG = STEPS_PER_REV/360
NUM_BEAKERS = 5

dir = OutputDevice(15)
pulse = OutputDevice(14)

dir.on()

for i in range(0,200):
    pulse.on()
    sleep(0.0005)
    pulse.off()

def rotate_deg(deg,motor):
    numSteps = deg * STEPS_PER_DEG
    
    for i in range(0,numSteps):
        pulse.on()
        sleep(0.001)
        pulse.off()
        sleep(0.001)

# Rotates the disk of beakers by the number of positions 
#def rotate_beakers(numPos):
#    currentAngle = s.value() * 180
#    newAngle = (numPos * angleBtwnBeakers) + currentAngle
#    s.angle(newAngle)
    

