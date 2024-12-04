from pypluto import pluto
from time import sleep

Drone = pluto()

Drone.connect()
sleep(1)

Drone.arm_deviate(throttle=1500)
sleep(2)

Drone.forward(2)
sleep(3)

Drone.reset_tilt()
sleep(1)

Drone.rcThrottle = 1100
sleep(1)

Drone.land()
sleep(1)

Drone.disconnect()
