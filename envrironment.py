import pyrosim
import random
import math
import numpy
import constants as c

class ENVIRONMENT:
    
    def __init__ (self,i):
        self.l = c.L
        self.w = c.L
        self.h = c.L
        self.ID = i
        
        
        if (self.ID == 0):
            self.Place_Light_Source_To_The_Front()
        if (self.ID == 1):
            self.Place_Light_Source_To_The_Right()
        if (self.ID == 2):
            self.Place_Light_Source_To_The_Back()
        if (self.ID ==3):
            self.Place_Light_Source_To_The_Left()
            
        #print("length: ",self.l, " width: ", self.w, " height: ", self.h, " position: x: ", self.x, " y: ", self.y, " z: ", self.z)
            
    def Place_Light_Source_To_The_Front(self):
        self.x = 0
        self.y = (30*c.L)
        self.z = (.5*c.L)
        
    def Place_Light_Source_To_The_Right(self):
        self.x = (30*c.L)
        self.y = 0
        self.z = (.5*c.L)
        
    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = (-30*c.L)
        self.z = (.5*c.L)
        
    def Place_Light_Source_To_The_Left(self):
        self.x = (-30*c.L)
        self.y = 0
        self.z = (.5*c.L)
        
    def Send_To(self, sim):
        #lightSource = sim.send_sphere(x = self.x, y = self.y, z = .25, radius = .25, r = 1, g = 0, b = 0)
        #sim.send_external_force(body_id = lightSource, x = self.y/7, y = self.x/7, z = 0, time=0)
        
        lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h, r=.5, g=.5, b=.5)
        sim.send_light_source( body_id = lightSource )
