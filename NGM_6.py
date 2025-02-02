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
    await drive_base.curve(1000,-15)
    await drive_base.curve(500,45)
    await drive_base.straight(150)
    await drive_base.curve(450,-20)
    await drive_base.curve(-600,-15)
    await drive_base.curve(-500,7)
    await drive_base.turn(-17)
    await drive_base.straight(250)
    await drive_base.straight(-300)
    await drive_base.turn(-35)
    await drive_base.curve(1350,100)                                  
# Runs the main program from start to finish.
run_task(main())