# TERASTIO PROGRAMMA

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

    await drive_base.straight(50)
    await drive_base.curve(132,45)
    await drive_base.curve(132,-90)
    await drive_base.straight(135)
    await multitask(right_motor.run_angle(200, 80), 
                    drive_base.straight(-150))
    await multitask(right_motor.run_angle(200, -80),
                    drive_base.straight(-170))

    await drive_base.curve(460, -55)
    await drive_base.turn(102)
    await drive_base.straight(-100)
    await multitask(right_motor.run_angle(200, 80),
                     drive_base.curve(1050, -20))
    await drive_base.turn(65)
    await drive_base.straight(150)
    await drive_base.straight(-125)
    await drive_base.turn(30)
    await drive_base.straight(140)
    await drive_base.straight(-125)
    await drive_base.curve(-110, 80)
    await drive_base.curve(120, -87)
    await drive_base.straight(480)
    await drive_base.turn(87) 
    await drive_base.straight(80)
    await left_motor.run_angle(200, -250)
    await drive_base.turn(-53) 
    await drive_base.curve(310, -87)
    await drive_base.straight(245)
    await drive_base.straight(-280)
    await multitask(left_motor.run_angle(200, 192),
                     drive_base.turn(50))
    await drive_base.straight(10)
    await drive_base.curve(500, 20)
    await drive_base.curve(140, -10)
    await drive_base.straight(50)
    await left_motor.run_angle(200, -200)
    await drive_base.straight(-200)
    await drive_base.turn(-72)
    await drive_base.straight(800)

    
                                             
# Runs the main program from start to finish.
run_task(main())