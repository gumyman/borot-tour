#!/usr/bin/env pybricks-micropython
# DONT DELETE LINE 1
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()
ev3.speaker.beep(frequency=100, duration=500)
ev3.speaker.beep(frequency=500, duration=500)

# Initialize motors
lmotor = Motor(Port.A)
rmotor = Motor(Port.B)

# Set speed limit for the right motor to 90% of max speed
lmotor.control.limits(900)

# Setting drive train - must be changed for every surface and bot design
drive = DriveBase(lmotor, rmotor, wheel_diameter=56, axle_track=116)

# Movement functions
def go(dist):
    drive.straight(dist * 500)

def tgo(deg, dist):
    if deg == -1:
        y = 91
    else:
        y=  89
    drive.turn(deg * y)
    go(dist)

def tar():
    drive.turn(184)

# Run movement sequence
drive.straight(375)
go(1)
tgo(1,1)
tgo(1,1)
tar()
go(1)
tgo(-1,1)
tgo(1,1)
tgo(-1,1)
tgo(1,1)
tgo(1,2)
tgo(1,1)
tar()
go(1)

tgo(-1,2)
tgo(-1,1)
go(1)
tgo(1,1)
go(1)
tgo(1,1)
tgo(1,1)
tar()
go(1)
tar(-1,1)
tar(-1,1)
