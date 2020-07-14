import pyrosim
import random
import math
import numpy
import constants as c
from prey import Prey


class PREY_INDIVIDUAL:
    def __init__(self,i):
       
        self.ID = i
        #create genome for the weight variable
        self.genome = c.evolvedGenomePrey
        
        #create fitness variable to store the quality of the individual
        self.fitness = 0
                
    
        
    def Mutate(self):
        
        row = random.randint(0,4)
        col = random.randint(0,3)
        self.genome[row, col] = random.gauss(self.genome[row,col] , math.fabs(self.genome[row,col]))
        
        if (self.genome[row,col] > 1):
            self.genome[row,col] = 1
            
        if (self.genome[row,col] < -1):
            self.genome[row,col] = -1
        
    def Start_Evaluation(self, env, pp, pb):
        #run simulator without pausing
        self.sim = pyrosim.Simulator(eval_time = c.evalTime, play_blind = pb, play_paused = pp)
        
        env.Send_To( self.sim )
        #create instance of the robot class
        #sends a random value between -1 and 1 for each iteration
        self.robot = Prey(self.sim, self.genome)
        
        self.collided = self.sim.assign_collision(self.robot, env.source)
        #start the simulator
        self.sim.start()
        
       
        
    
    def Compute_Fitness(self):
        
        self.sim.wait_to_finish()
   
        #get sensor data for the ray sensor
        #B is 1 or 0 whether the ray is detecting a blue object
        self.B = self.sim.get_sensor_data(sensor_id = self.robot.R, svi = 3)
        self.avgB = numpy.average(self.B)
        #D is the distance of the ray (shorter means closer)
        self.D = self.sim.get_sensor_data(sensor_id = self.robot.R, svi = 0)
        self.avgD = numpy.average(self.D)
       
        self.fitness = self.fitness + (self.avgB * self.avgD)
        
        #extract the position sensor
        self.position = self.sim.get_sensor_data(sensor_id = self.robot.position)
        
        del (self.sim)
        
    
    def Print(self):
        print('[', self.ID, " ", self.fitness, "]", end = "")

       
        