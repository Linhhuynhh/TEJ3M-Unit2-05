#! usr/bin/env python3
"""
Created by: Linh Huynh
Created on: Mar 2025
"""

import time
import board
import pwmio
from adafruit_motor
import servo

# create a PWMOut object on Pin A8.
pwm = pwmio.PWMOut(board.A2, duty_cycle=8 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
