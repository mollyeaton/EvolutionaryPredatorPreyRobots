import pyrosim
import random
import math
import numpy
import constants as c
from predator import Predator
from prey import Prey


class COMBINED_PAIR:
    def __init__(self,i):
       
        self.ID = i
        #create genome for the weight variable
        self.predatorGenome = c.evolvedGenomePredator
        self.preyGenome = c.evolvedGenomePrey
        
        #create fitness variable to store the quality of the individual
        self.preyFitness = 0
        self.predatorFitness = 0
                
    
        
    def Mutate(self):
        
        row = random.randint(0,4)
        col = random.randint(0,3)
        self.predatorGenome[row, col] = random.gauss(self.predatorGenome[row,col] , math.fabs(self.predatorGenome[row,col]))
        
        if (self.predatorGenome[row,col] > 1):
            self.predatorGenome[row,col] = 1
            
        if (self.predatorGenome[row,col] < -1):
            self.predatorGenome[row,col] = -1
        
        row = random.randint(0,4)
        col = random.randint(0,3)
        self.preyGenome[row, col] = random.gauss(self.preyGenome[row,col] , math.fabs(self.preyGenome[row,col]))
        
        if (self.preyGenome[row,col] > 1):
            self.preyGenome[row,col] = 1
            
        if (self.preyGenome[row,col] < -1):
            self.preyGenome[row,col] = -1
        
    def Start_Evaluation(self, pp, pb):
        #run simulator without pausing
        self.sim = pyrosim.Simulator(eval_time = c.evalTime, play_blind = pb, play_paused = pp)
        
        
        #create instance of the robot class
        #sends a random value between -1 and 1 for each iteration
        self.predator = Predator(self.sim, self.predatorGenome)
        self.prey = Prey(self.sim, self.preyGenome)
        
        
        #start the simulator
        self.sim.start()
        
       
        
    
    def Compute_Fitness(self):
        
        self.sim.wait_to_finish()
   
    
        preyRay = self.sim.get_sensor_data(sensor_id = self.prey.R, svi = 3)
        avgPreyRay = numpy.average(preyRay)
        preyD = self.sim.get_sensor_data(sensor_id = self.prey.R, svi = 0)
        avgPreyD = numpy.average(preyD)
        
        
        
        predatorRay = self.sim.get_sensor_data(sensor_id = self.predator.R, svi = 1)
        avgPredatorRay = numpy.average(predatorRay)
        predatorD = self.sim.get_sensor_data(sensor_id = self.predator.R, svi = 0)
        avgPredatorD = numpy.average(predatorD)
       
        self.fitness =  ((avgPreyRay * avgPreyD) + (avgPredatorRay * (1/avgPredatorD)))/2
        
        
        del (self.sim)
        
    
    def Print(self):
        print('[', self.ID, " ", self.fitness, "]", end = "")

       
        