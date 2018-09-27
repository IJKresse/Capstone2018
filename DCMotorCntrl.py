from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice

en = OutputDevice(2) # Pin number for enable
pwm = PWMOutputDevice(3, 1000) # Pin number for PWM, frequency

# Turn on enable
en.on()

# Turn on w/ default value of 0
pwm.on()
pwm.value = 0.5 # Duty cycle to 50%
