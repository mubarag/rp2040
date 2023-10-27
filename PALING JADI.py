# Raspberry Pi Pico based Line Following Robot
from machine import Pin,PWM #importing PIN and PWM
import time #importing time
import utime
# Defining motor pins
motor1=Pin(8,Pin.OUT)
motor2=Pin(9,Pin.OUT)
motor3=Pin(10,Pin.OUT)
motor4=Pin(11,Pin.OUT)
# Defining enable pins and PWM object
enable1=PWM(Pin(6))
enable2=PWM(Pin(7))
# Defining  right and left IR digital pins as input
right_ir = Pin(2, Pin.IN)
left_ir = Pin(26, Pin.IN)
# Defining frequency for enable pins
enable1.freq(1000)
enable2.freq(1000)
# Setting maximum duty cycle for maximum speed
enable1.duty_u16(65025)
enable2.duty_u16(65025)
# Forward
def move_forward():
    motor1.low()
    motor2.high()
    motor3.high()
    motor4.low() 
# Backward
def move_backward():
    motor1.high()
    motor2.low()
    motor3.low()
    motor4.high() 
#Turn Right
def turn_right():
    motor1.low()
    motor2.high()
    motor3.low()
    motor4.high()
    
#Turn Left
def turn_left():
    motor1.high()
    motor2.low()
    motor3.high()
    motor4.low()
    

#Stop
def stop():
    motor1.low()
    motor2.low()
    motor3.low()
    motor4.low()
    
    
while True:
    right_val=right_ir.value() #Getting right IR value(0 or 1)
    left_val=left_ir.value() #Getting left IR value(0 or 1)  
    print(str(right_val)+"-"+str(left_val))
    # Controlling robot direction based on IR value 
    if right_val==0 and left_val==0:
        move_forward()
    elif right_val==1 and left_val==0:
        turn_right()
    elif right_val==0 and left_val==1:
        turn_left()
    elif right_val == 1 and left_val == 1:  # Both sensors are active
        # Add code to turn right when both sensors are active
        turn_right()
    else:
        stop()
