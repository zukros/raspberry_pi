import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11, 50)


duty=2
pwm.start(0)
pwm.ChangeDutyCycle(7.5) # Middle
sleep(1)
pwm.ChangeDutyCycle(2) #-90/right
sleep(1)
pwm.ChangeDutyCycle(12) #180/left
sleep(1)

pwm.stop()
GPIO.cleanup()
print ("Goodbye")

