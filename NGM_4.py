# TRIAINA - KARXARIAS

from pybricks.hubs import PrimeHub 
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor 
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop 
from pybricks.robotics import DriveBase  
from pybricks.tools import wait, multitask, run_task  

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y) 

right_wheel = Motor(Port.B)
left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)    # default positive direction is clockwise 
left_motor = Motor(Port.E)
right_motor = Motor(Port.A)

drive_base = DriveBase(left_wheel, right_wheel, 62, 120)
drive_base.use_gyro(True)
drive_base.settings(500, 600, 220, 300)
# drive_base.settings(1000, 1000, 1000, 1000)

# Drive forward, turn move gripper at the same time, and drive backward.
async def main():
    await multitask(drive_base.straight(670),
                    right_motor.run_angle(100, 100),
                    left_motor.run_angle(200, 300))
    await drive_base.turn(-49)
    await drive_base.straight(205)
    await left_motor.run_angle(300, -450)
    await drive_base.straight(-25)
    await drive_base.straight(27)
    await left_motor.run_angle(150, 400)
    await drive_base.straight(-150)
    await drive_base.turn(-48)
    await drive_base.straight(150)
    await drive_base.turn(-110)
    drive_base.settings(1000, 1000, 220, 300)
    await drive_base.straight(600)

    


# Runs the main program from start to finish.
run_task(main())