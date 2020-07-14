import pyrosim
import matplotlib.pyplot as plt
import random
import numpy

import constants as c

class Prey:
    
    def __init__(self, sim, wts):
        
        #run modulated code to create the robot and necessary peripherals
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)
        
        #delete dictionaries
        #del self.O
        del self.J
        del self.S
        del self.SN
        del self.MN
        
        
        
    def send_objects(self, sim):
        
        #create objects that make up the robot and send to simulator
        #body is the main chasis of the robot
        self.body = sim.send_box( x=1 , y=0 , z=(c.L/2)+c.wR , length=c.L ,width = c.L, height = c.L , r = 1, g = 0, b=0)
        #4 axels for the wheels (actuators will be sent to these to rotate the spheres)
        #RF = right front ; RB = right back ; LF = left front ; LB = left back
        self.axelRF = sim.send_cylinder(x=1+(1/2)*c.L, y=(1/4)*c.L, z=(2/3)*c.wR, r1=1, r2=0, r3=0, r=1, g=0, b=0, capped = False, length=(1/2)*c.L, radius= (1/3)*c.wR)
        self.axelRB = sim.send_cylinder(x=1+(1/2)*c.L, y=(-1/4)*c.L, z=(2/3)*c.wR, r1=1, r2=0, r3=0, r=1, g=0, b=0, capped = False, length=(1/2)*c.L, radius= (1/3)*c.wR)
        self.axelLF = sim.send_cylinder(x=1+(-1/2)*c.L, y=(1/4)*c.L, z=(2/3)*c.wR, r1=1, r2=0, r3=0, r=1, g=0, b=0, capped = False, length=(1/2)*c.L, radius= (1/3)*c.wR)
        self.axelLB = sim.send_cylinder(x=1+(-1/2)*c.L, y=(-1/4)*c.L, z=(2/3)*c.wR, r1=1, r2=0, r3=0, r=1, g=0, b=0, capped = False, length=(1/2)*c.L, radius= (1/3)*c.wR)
        #4 wheels
        self.wheelRF = sim.send_sphere(x = 1+(1/2)*c.L +c.wR, y = (1/4)*c.L, z = c.wR, radius = c.wR, r1 = 0, r2 = 0, r3 = 1, r = 1, g=0, b=0)
        self.wheelRB = sim.send_sphere(x = 1+(1/2)*c.L +c.wR, y = (-1/4)*c.L, z = c.wR, radius = c.wR, r1 = 0, r2 = 0, r3 = 1,r = 1, g=0, b=0)
        self.wheelLF = sim.send_sphere(x = 1+(-1/2)*c.L -c.wR, y = (1/4)*c.L, z = c.wR, radius = c.wR, r1 = 0, r2 = 0, r3 = 1, r = 1, g=0, b=0)
        self.wheelLB = sim.send_sphere(x = 1+(-1/2)*c.L -c.wR, y = (-1/4)*c.L, z = c.wR, radius = c.wR, r1 = 0, r2 = 0, r3 = 1, r = 1, g=0, b=0)
        
        
    def send_joints(self, sim):

        #create joint fixing the axels to the body
        self.fj0 = sim.send_fixed_joint( first_body_id = self.body , second_body_id = self.axelRF)
        self.fj1 = sim.send_fixed_joint( first_body_id = self.body , second_body_id = self.axelRB)
        self.fj2 = sim.send_fixed_joint( first_body_id = self.body , second_body_id = self.axelLF)
        self.fj3 = sim.send_fixed_joint( first_body_id = self.body , second_body_id = self.axelLB)
        
        #create rotating joints for wheels to move foreward
        self.wj0 = sim.send_hinge_joint(first_body_id=self.axelRF, second_body_id=self.wheelRF, x=1+(1/2)*c.L,  y=(1/4)*c.L, z=c.wR, n1=-1, n2=0, n3=0, position_control=False, speed = 3)
        self.wj1 = sim.send_hinge_joint(first_body_id=self.axelRB, second_body_id=self.wheelRB, x=1+(1/2)*c.L, y=(-1/4)*c.L, z=c.wR, n1=-1, n2=0, n3=0, position_control=False, speed = 3)
        self.wj2 = sim.send_hinge_joint(first_body_id=self.axelLF, second_body_id=self.wheelLF, x=1+(-1/2)*c.L, y=(1/4)*c.L, z=c.wR, n1=-1, n2=0, n3=0, position_control=False, speed = 3)
        self.wj3 = sim.send_hinge_joint(first_body_id=self.axelLB, second_body_id=self.wheelLB, x=1+(-1/2)*c.L, y=(-1/4)*c.L, z=c.wR, n1=-1, n2=0, n3=0, position_control=False, speed = 3)


    def send_sensors(self, sim):
        
        #create touch sensors for wheels
        self.T0 = sim.send_touch_sensor( body_id = self.wheelRF )
        self.T1 = sim.send_touch_sensor( body_id = self.wheelRB )
        self.T2 = sim.send_touch_sensor( body_id = self.wheelLF )
        self.T3 = sim.send_touch_sensor( body_id = self.wheelLB )
        
        #create a light sensor so the robot will be able to detect the other
        self.R = sim.send_ray_sensor(body_id=self.body, x=1, y=c.L/2, z=(c.L/2)+c.wR, r1=0, r2=1, r3=0, max_distance=10)
        self.position = sim.send_position_sensor(body_id = self.body)

    def send_neurons(self, sim):
        
        #create a dictionary for the sensors
        self.S = {}
        #fill the dictionary
        self.S[0] = self.T0
        self.S[1] = self.T1
        self.S[2] = self.T2
        self.S[3] = self.T3
        self.S[4] = self.R
        
        #create a dictionary to hold the joints
        self.J = {}
        self.J[0] = self.wj0
        self.J[1] = self.wj1
        self.J[2] = self.wj2
        self.J[3] = self.wj3
        
        #empty dictionaries for the sensor/motor neurons
        self.SN = {}
        self.MN = {}
        
        #loop through and send sensor neurons while filling the dict
        for s in self.S:

            self.SN[s] = sim.send_sensor_neuron(self.S[s])

        #loop through and send motor neurons while filling the dict
        for j in self.J:

            self.MN[j] = sim.send_motor_neuron(self.J[j])
            
           
    def send_synapses(self,sim, wts):
        
        for j in self.SN:

            for i in self.MN:

                sim.send_synapse(source_neuron_id = self.SN[j] , target_neuron_id = self.MN[i], weight = wts[j,i] )   


#sim.send_synapse(source_neuron_id = SN0 , target_neuron_id = MN2 , weight = -1.0 )


