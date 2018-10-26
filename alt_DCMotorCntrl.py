from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice
from time import sleep
import RPi.GPIO as GPIO

dir1 = OutputDevice(3)
dir2 = OutputDevice(4)

en_pwm = PWMOutputDevice(27, 1000)
##en = OutputDevice(2) # Pin number for enable
##pwm = PWMOutputDevice(3, 1000) # Pin number for PWM, frequency

dir2.off()
dir1.on()

# Turn on w/ default value of 0
en_pwm.value = 0.05
##en_pwm.on()
sleep(2)
en_pwm.value = 0.1
sleep(2)
en_pwm.value = 0.3
sleep(2)
en_pwm.value = 0
en_pwm.off()

GPIO.cleanup()