# Outputs: throttle, roll, pitch, yaw
# Inputs: Image(angx, angy, heading), ultrasonic sensor?, gps?, compass?


# DronePilot in repo but used only for reference
	# import DronePilot

# Tools/outside scripts
import pymultiwii
import opencv
# Python library
import gpiozero

# output = throttle, roll, pitch, yaw
# Set a GPIO pin to a specific PWM for each output
throttle = GPIO.PWM(channel, freq)
roll = GPIO.PWM(channel, freq)
pitch = GPIO.PWM(channel, freq)
yaw = GPIO.PWM(channel, freq)


# Direction changes and adjustment
midpoint = [0,0]
# heading starts at 100 and ends at 0 once it reaches destination
heading = 100
changeInX = midpoint[0] + angX
changeInY = midpoint[1] + angY

# Adjust flight path based on changes in X and Y
adjustX = -changeInX
adjustY = -changeInY

# ***DON'T KNOW WHERE THIS STUFF GOES YET***
		throttle.ChangeFrequency(freq)
		throttle.ChangeDutyCycle(dc)
		roll.ChangeFrequency(freq)
		roll.ChangeDutyCycle(dc)
		pitch.ChangeFrequency(freq)
		pitch.ChangeDutyCycle(dc)
		yaw.ChangeFrequency(freq)
		yaw.ChangeDutyCycle(dc)


def arm(throttle, roll, pitch, yaw)
	throttle.start(dc)
	roll.start(dc)
	pitch.start(dc)
	yaw.start(dc)
return;

def disarm(throttle, roll, pitch, yaw)
	throttle.stop()
	roll.stop()
	pitch.stop()
	yaw.stop()
return;


	





