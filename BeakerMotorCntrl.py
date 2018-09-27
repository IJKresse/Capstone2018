from gpiozero import AngularServo
s = AngularServo(17, min_angle = -180, max_angle = 180) # GPIO pin number
NUM_BEAKERS = 5;
angleBtwnBeakers = 360/NUM_BEAKERS

# Rotates the disk of beakers by the number of positions 
def rotate_beakers(numPos):
    currentAngle = s.value() * 180
    newAngle = (numPos * angleBtwnBeakers) + currentAngle
    s.angle(newAngle)
    

