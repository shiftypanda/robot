# Edukit 3 robootics, motor test code

import time
from gpiozero import CamJamKitRobot
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.1.3')

robot = CamJamKitRobot(pin_factory=factory)

# turn the motors on
robot.forward()

# wait for 1 seconds
time.sleep(1)

# turn the motors off
robot.stop()
