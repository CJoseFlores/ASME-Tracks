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

	def TurnLeft(self):
		for i in range(self.__rightPosNext, self.__rightPosCurrent, -1):
			DC = ((1. / 18.) * i) + 2
			self.__pwm1.ChangeDutyCycle(DC)
			self.__pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		self.__rightPosNext = self.__rightPosCurrent
		self.__leftPosNext = self.__leftPosCurrent
		self.__rightPosCurrent -= 1
		self.__leftPosCurrent -= 1
		if self.__rightPosNext == 0:
			self.__leftPosCurrent = 359
			self.__rightPosCurrent = 359
			self.__leftPosNext = 360
			self.__rightPosNext = 360

	def Reverse(self):
		for i in range(self.__rightPosCurrent, self.__rightPosNext, 1):
			DC = ((1. / 18.) * i) + 2
			self.__pwm1.ChangeDutyCycle(DC)
			time.sleep(0.02)
		self.__rightPosCurrent = self.__rightPosNext
		self.__rightPosNext += 1
		if self.__rightPosCurrent == 360:
			self.__rightPosCurrent = 0
			self.__rightPosNext = 1
		for i in range(self.__leftPosNext, self.__leftPosCurrent, -1):
			DC = ((1. / 18.) * i) + 2
			self.__pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		self.__leftPosNext = self.__leftPosCurrent
		self.__leftPosCurrent -= 1
		if self.__leftPosNext == 0:
			self.__leftPosNext = 360
			self.__leftPosCurrent = 359

	def Forward(self):
		for i in range(self.__rightPosNext, self.__rightPosCurrent, -1):
			DC = ((1. / 18.) * i) + 2
			self.__pwm1.ChangeDutyCycle(DC)
			time.sleep(0.02)
		self.__rightPosNext = self.__rightPosCurrent
		self.__rightPosCurrent -= 1
		if self.__rightPosNext == 0:
			self.__rightPosNext = 360
			self.__rightPosCurrent = 359
		for i in range(self.__leftPosCurrent, self.__leftPosNext, 1):
			DC = ((1. / 18.) * i) + 2
			self.__pwm2.ChangeDutyCycle(DC)
			time.sleep(0.02)
		self.__leftPosCurrent = self.__leftPosNext
		self.__leftPosNext += 1
		if self.__leftPosCurrent == 360:
			self.__leftPosCurrent = 0
			self.__leftPosNext = 1
	

pwm1.stop()
pwm2.stop()
