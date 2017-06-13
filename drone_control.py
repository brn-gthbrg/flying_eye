import pymultiwii
import opencv
import gpiozero

# Set PWM for each output
# Adjust PWM based on inputs
p = GPIO.PWM(channel, freq)
p.start(dc)
p.ChangeFrequency(freq)
p.ChangeDutyCycle(dc)
p.stop()

# Outputs: throttle, roll, pitch, yaw
# Inputs: Image(angx, angy, heading), ultrasonic sensor, gps, bluetooth