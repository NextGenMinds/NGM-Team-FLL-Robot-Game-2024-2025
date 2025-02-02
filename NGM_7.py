# FALENA

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

    # await drive_base.straight(-710)
    # await drive_base.turn(32)
    # await drive_base.straight(-150)
    # await drive_base.straight(220)
    # await drive_base.turn(68)
    # await drive_base.straight(270)
    # await drive_base.turn(25)
    # await drive_base.straight(110)
    # await right_motor.run_angle(400, -1200)
    # await drive_base.turn(-60)
    # await drive_base.straight(110)
    # await drive_base.turn(92)
    # await multitask(drive_base.straight(200),
    #                 left_motor.run_angle(400, 200)
    #                 )
    # await left_motor.run_angle(400, -200)

    await drive_base.curve(-1500,27)
    await drive_base.turn(70)
    await drive_base.straight(-160)
    await drive_base.straight(210)
    await drive_base.turn(57)
    await drive_base.straight(210)
    await right_motor.run_angle(400, -1200)
    await multitask(drive_base.curve(200, 40),
                    left_motor.run_angle(400, 200)
                    )
    await drive_base.straight(120)
    await left_motor.run_angle(400, -200)
    
                                             
# Runs the main program from start to finish.
run_task(main())