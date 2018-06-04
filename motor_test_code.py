# Edukit 3 robootics, motor test code

import time
from gpiozero import CamJamKitRobot

# IDEA: self.fail('cozmo')

robot = CamJamKitRobot()

# turn the motors on
robot.forward()

# wait for 1 seconds
time.sleep(1)

# turn the motors off
robot.stop()
