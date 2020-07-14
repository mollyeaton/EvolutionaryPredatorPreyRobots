import pyrosim
import random
import math
import numpy
import constants as c

class MOVING_ENVIRONMENT:
    
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
        self.y = (30*c.D)
        self.z = (.25)
        
    def Place_Light_Source_To_The_Right(self):
        self.x = (30*c.D)
        self.y = 0
        self.z = (.25)
        
    def Place_Light_Source_To_The_Back(self):
        self.x = 0
        self.y = (-30*c.D)
        self.z = (.25)
        
    def Place_Light_Source_To_The_Left(self):
        self.x = (-30*c.D)
        self.y = 0
        self.z = (.25)
        
    def Send_To(self, sim):
        self.source = sim.send_sphere(x = self.x, y = self.y, z = .25, radius = .25, r = c.red, g = 0, b = c.blue)
        if (self.x == 0):
            sim.send_external_force(body_id = self.source, x = 2, y = 0, z = 0, time=0)
        else:
            sim.send_external_force(body_id = self.source, x = 0, y = 2, z = 0, time=0)

