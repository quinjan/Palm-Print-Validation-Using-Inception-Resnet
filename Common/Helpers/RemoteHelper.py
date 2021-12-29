# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:35:24 2021

@author: quinj
"""

import socket
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

class RemoteHelper():
    def __init__(self):
        self.ipv4 = socket.gethostbyname('raspberrypi')
        self.videoFeed = "http://{0}:5000/video_feed".format(self.ipv4)
    
    def InitializeGPIOPins(self):
        print("Initializing Pins for Flash")
        self.factory = PiGPIOFactory(host=self.ipv4)
        self.leftPin = LED(23,pin_factory=self.factory)
        self.rightPin = LED(24,pin_factory=self.factory)
    
    def RunFlash(self):
        self.leftPin.on()
        self.rightPin.on()
    
    def StopFlash(self):
        print("Stopping Flash")
        self.leftPin.off()
        self.rightPin.off()
       
        
        