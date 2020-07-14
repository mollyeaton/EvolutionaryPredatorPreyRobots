import copy
from random import randint
from predatorIndividual import PREDATOR_INDIVIDUAL

class PREDATOR_POPULATION:
    #constructor
    def __init__(self, popSize):
        
        self.popSize = popSize
        self.p = {}
        
        
    def Print(self):
        
        for i in self.p:
            if ( i in self.p ):
                self.p[i].Print()
            
        print("")
            
    def Evaluate(self, envs, pp, pb):
        for i in self.p:
            self.p[i].fitness = 0
            
        for e in envs.envs:
            for i in self.p:         
                self.p[i].Start_Evaluation(envs.envs[e], pp, pb)
            
            for i in self.p:
                self.p[i].Compute_Fitness()
            
        for i in self.p:
            self.p[i].fitness = self.p[i].fitness/len(envs.envs)
    def Mutate(self):
        
        for i in self.p:
            self.p[i].Mutate()
            
    def ReplaceWith(self,other):
        
        for i in self.p:
            
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]
                
    def Initialize(self):
        
        for i in range(0,self.popSize):

            self.p[i] = PREDATOR_INDIVIDUAL(i)
            
            
    def Fill_From(self , other):
        
        self.Copy_Best_From(other)
        
        
        self.Collect_Children_From(other)
        
        
    def Copy_Best_From(self, other):
        self.best = other.p[0].fitness
        index = 0
        for i in other.p:
            if (other.p[i].fitness > self.best):
                self.best = other.p[i].fitness
                index = i
        
        self.p[0] = copy.deepcopy(other.p[index])
        return index
    
    def Collect_Children_From(self, other):
        
        for i in range(1,len(other.p)):
            winner = other.Winner_Of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()
            
            
    def Winner_Of_Tournament_Selection(other):
        
        p1 = randint(0,len(other.p)-1)
        p2 = randint(0,len(other.p)-1)
        while (p1 == p2):
            p2 = randint(0, len(other.p)-1)
                     
        if(other.p[p1].fitness > other.p[p2].fitness):
            return other.p[p1]
        else:
            return other.p[p2]
        
        
            
        
                
                
                
                
                
        