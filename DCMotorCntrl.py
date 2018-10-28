from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice
from time import sleep

en = OutputDevice(27) # Pin number for enable
pwm = PWMOutputDevice(3, 1000) # Pin number for PWM, frequency


# Turn on enable
en.on()

# Turn on w/ default value of 0
pwm.on()
pwm.value = 0.05 # Duty cycle to 50%
sleep(2)
pwm.value = 0.1
sleep(2)
pwm.value = 0.25
sleep(2)
pwm.off()
