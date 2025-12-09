from microbit import *
import kitronik_motor_driver

# Turn off motor at start
kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)

# Function to move servo on SV1
def set_servo_sv1(angle):
    # SV1 is wired to pin0
    pulse = 500 + (angle * 2000 // 180)  # 0° -> 500µs, 180° -> 2500µs
    pin0.set_analog_period_microseconds(20000)
    duty = pulse * 1023 // 20000
    if duty < 0: duty = 0
    if duty > 1023: duty = 1023
    pin0.write_analog(duty)

# Button callbacks
def on_button_pressed_a():
    set_servo_sv1(90)   # rotate to 90°
    sleep(50)

def on_button_pressed_b():
    set_servo_sv1(0)    # rotate to 0°
    sleep(50)

# Register button callbacks
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Keep program running
while True:
    sleep(100)
