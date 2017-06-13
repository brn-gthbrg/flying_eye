import pymultiwii
import opencv
import gpiozero

p = GPIO.PWM(channel, freq)
p.start(dc)
p.ChangeFrequency(freq)
p.ChangeDutyCycle(dc)
p.stop()

# Outputs: throttle, roll, pitch, yaw
# Inputs: angx, angy, heading