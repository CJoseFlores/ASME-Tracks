import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class DualServos:
	__DataPin1 = None
	__DataPin2 = None
	__pwm1 = None
	__pwm2 = None
	__leftPosCurrent = 0
	__leftPosNext = 1
	__rightPosCurrent = 0
	__rightPosNext = 1

	def __init__(self, servopin1, servopin2):
		self.__DataPin1 = servopin1
		self.__DataPin2 = servopin2
		GPIO.setup(self.__DataPin1, GPIO.OUT)
		GPIO.setup(self.__DataPin2, GPIO.OUT)
		self.__pwm1 = GPIO.PWM(self.__DataPin1, 50)
		self.__pwm2 = GPIO.PWM(self.__DataPin2, 50)
		self.__pwm1.start(0)
		self.__pwm2.start(0)

	def TurnRight(self):
		for i in range(self.__rightPosCurrent, self.__rightPosNext, 1):
			DC = ((1. / 18.) * i) + 2
			self.__pwm1.ChangeDutyCycle(DC)
			self.__pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		self.__leftPosCurrent = self.__leftPosNext
		self.__rightPosCurrent = self.__rightPosNext
		self.__leftPosNext += 1
		self.__rightPosNext += 1
		if self.__rightPosCurrent == 360:
			self.__rightPosCurrent = 0
			self.__leftPosCurrent = 0
			self.__rightPosNext = 1
			self.__leftPosNext = 1

while (1):


	#while(fileRight == 1):
		for i in range(rightPosCurrent, rightPosNext, 1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		leftPosCurrent = leftPosNext
		rightPosCurrent = rightPosNext
		leftPosNext += 1
		rightPosNext += 1
		if rightPosCurrent == 360:
			rightPosCurrent = 0
			leftPosCurrent = 0
			rightPosNext = 1
			leftPosNext = 1
		tempRight = open('Right', 'r')
		fileRight = int(tempRight.read())

	#while(fileLeft == 1):
		for i in range(rightPosNext, rightPosCurrent, -1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		rightPosNext = rightPosCurrent
		leftPosNext = leftPosCurrent
		rightPosCurrent -= 1
		leftPosCurrent -= 1
		if rightPosNext == 0:
			leftPosCurrent = 359
			rightPosCurrent = 359
			leftPosNext = 360
			rightPosNext = 360 
		tempLeft = open('Left', 'r')
		fileLeft = int(tempLeft.read())

	#while(fileReverse == 1):
		for i in range(rightPosCurrent, rightPosNext, 1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			time.sleep(0.02)
		rightPosCurrent = rightPosNext
		rightPosNext += 1
		if rightPosCurrent == 360:
			rightPosCurrent = 0
			rightPosNext = 1
		for i in range(leftPosNext, leftPosCurrent, -1):
			DC = ((1./18.) * i) + 2
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		leftPosNext = leftPosCurrent
		leftPosCurrent -= 1
		if leftPosNext == 0:
			leftPosNext = 360
			leftPosCurrent = 359
		tempReverse = open('Reverse', 'r')
		fileReverse = int(tempReverse.read())

	#while(fileForward == 1):
		for i in range(rightPosNext, rightPosCurrent, -1):
			DC = ((1./18.) * i) + 2
			pwm1.ChangeDutyCycle(DC)
			time.sleep(0.02)
		rightPosNext = rightPosCurrent
		rightPosCurrent -= 1
		if rightPosNext == 0:
			rightPosNext = 360
			rightPosCurrent = 359
		for i in range(leftPosCurrent, leftPosNext, 1):
			DC = ((1./18.) * i) + 2
			pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		leftPosCurrent = leftPosNext
		leftPosNext += 1
		if leftPosCurrent == 360:
			leftPosCurrent = 0
			leftPosNext = 1
		tempForward = open('Forward', 'r')
		fileForward = int(tempForward.read())

	#while(fileRoam == 1):
		for j in range(0, 30, 1):
			for i in range(rightPosNext, rightPosCurrent, -1):
				DC = ((1./18.) * i) + 2
				pwm1.ChangeDutyCycle(DC)
				time.sleep(0.02)
			rightPosNext = rightPosCurrent
			rightPosCurrent -= 1
			if rightPosNext == 0:
				rightPosNext = 360
				rightPosCurrent = 359
			for i in range(leftPosCurrent, leftPosNext, 1):
				DC = ((1./18.) * i) + 2
				pwm2.ChangeDutyCycle(DC)
				time.sleep(0.02)
			leftPosCurrent = leftPosNext
			leftPosNext += 1
			if leftPosCurrent == 360:
				leftPosCurrent = 0
				leftPosNext = 1
		randValue = randrange(361, 720)
		for j in range(0, randValue, 1):
			for i in range(leftPosCurrent, leftPosNext, 1):
				DC = ((1./18.) * i) + 2)
				pwm1.ChangeDutyCycle(DC)
				pwm2.ChangeDutyCycle(DC)
				sleep.time(0.02)
			rightPosCurrent = rightPosNext
			leftPosCurrent = leftPosNext
			rightPosNext += 1
			leftPosNext += 1
			if rightPosCurrent == 360:
				rightPosCurrent = 0
				rightPosNext = 1
				leftPosCurrent 0
				leftPosNext = 1
		tempRoam = open('Roam', 'r')
		fileRoam = int(tempRoam.read())
	

pwm1.stop()
pwm2.stop()
