from controller import Robot, Motor, Camera
from math import pi, sin
import numpy as np
import time
import cv2

timeStep = 32

robot = Robot()

robot.step(10) #this needs to be at the start of every script


#CAMERA SECTION
tcam = robot.getDevice('CameraTop')
bcam = robot.getDevice('CameraBottom')

#enable the cameras
tcam.enable(timeStep)
bcam.enable(timeStep)

#COMPUTER VISION SECTION
cv2.startWindowThread()
cv2.namedWindow("preview")


# #MOVEMENT SECTION
motor = robot.getDevice("RShoulderPitch")

F = 2.0   # frequency 2 Hz
t = 0.0   # elapsed simulation time

while (robot.step(timeStep) != -1):
    
    #CAMERA SECTION
    cameraData = tcam.getImage()
    
    # tcam.saveImage("top.jpg",100) #save as jpg, it's faster
    # bcam.saveImage("bot.jpg",100)
    cameraData = tcam.getImage()
    image = np.frombuffer(cameraData, np.uint8).reshape((tcam.getHeight(), tcam.getWidth(), 4))
 
    #CV SECTION   
    cv2.imshow("preview", image)
    cv2.waitKey(timeStep)
    
    #MOTION SECTION
    # position = sin(t * 2.0 * pi * F)
    # motor.setPosition(position)
    # t += timeStep / 1000.0
    
    