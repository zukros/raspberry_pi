import RPi.GPIO as GPIO
from time import sleep
import time
import numpy as np


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)


try:
    while 1:
        for i in np.arange(1, 11.5, 0.1):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.01)
            print("AntiClockwise: ", i)
            
        for i in np.arange(11, 0.5, -0.1):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.01)
            print("ClockWise: ", i)
except KeyboardInterrupt: 
     pass


pwm.stop()
GPIO.cleanup()
print ("Done")

