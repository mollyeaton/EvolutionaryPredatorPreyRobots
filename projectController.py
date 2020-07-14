import pyrosim
import matplotlib.pyplot as plt
import numpy

from prey import Prey
from predator import Predator

from preyIndividual import PREY_INDIVIDUAL
from predatorIndividual import PREDATOR_INDIVIDUAL

from preyPopulation import PREY_POPULATION
from predatorPopulation import PREDATOR_POPULATION

from combined import COMBINED_PAIR
from combinedPopulation import COMBINED_POPULATION

from stationaryEnvironments import STATIONARY_EVIRONMENTS
from movingEnvironments import MOVING_ENVIRONMENTS

import constants as c

fitness = []

#######################################################################################################
print ("EVOLVING PREDATOR FOR STATIONARY LIGHT SOURCE")

envs = STATIONARY_EVIRONMENTS()

parents = PREDATOR_POPULATION(c.popSize)

parents.Initialize()

parents.Evaluate(envs, pp=False, pb=True)
print (0, end = " ")
parents.Print()


for g in range(1, c.numGens+1):
    children = PREDATOR_POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp = False, pb =True)
    print(g, end = " ")
    children.Print()
    
    parents.ReplaceWith(children)
    fitness.append(parents.p[0].fitness)
    
#c.evolvedGenomePredator = parents.p[0].genome    

"""
parents.p[0].Start_Evaluation(envs.envs[0], pp = True, pb = False)
parents.p[0].Compute_Fitness()

#plot the distance of the ray
f = plt.figure()

panel = f.add_subplot(111)
plt.title("Stationary Target in Front - Predator Post-Evolution")
plt.xlabel("Time Step")
plt.ylabel("Length of Ray Sensor")
plt.plot(parents.p[0].D)

plt.show()
parents.p[0].Start_Evaluation(envs.envs[1], pp = False, pb = True)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[2], pp = False, pb = True)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[3], pp = False, pb = True)
parents.p[0].Compute_Fitness()

#plot the distance of the ray
f = plt.figure()

panel = f.add_subplot(111)
plt.title("Stationary Target Behind - Predator Post-Evolution")
plt.xlabel("Time Step")
plt.ylabel("Length of Ray Sensor")
plt.plot(parents.p[0].D)

plt.show()

print("EVOLVED PREDATOR GENOME FOR STATIONARY LIGHT SOURCE")
print(c.evolvedGenomePredator)

f = plt.figure()

panel = f.add_subplot(111)
plt.title("Evolving Fitness for Predator with Stationary Objects")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.plot(fitness)

plt.show()
"""
c.D = .01
c.red = 0
c.blue = 1
c.preyX = 1


#######################################################################################################
print("EVOLVING PREY FOR STATIONARY LIGHT SOURCE")

envs = STATIONARY_EVIRONMENTS()

parents = PREY_POPULATION(c.popSize)

parents.Initialize()
parents.Evaluate(envs, pp = False, pb = True)
print(0, end = " ")
parents.Print()

for g in range(1, c.numGens+1):
    children = PREY_POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp = False, pb =True)
    print(g, end = " ")
    children.Print()
    
    parents.ReplaceWith(children)
    fitness.append(parents.p[0].fitness)


#c.evolvedGenomePrey = parents.p[0].genome    
"""
parents.p[0].Start_Evaluation(envs.envs[0], pp = True, pb = False)
parents.p[0].Compute_Fitness()

#plot the distance of the ray
f = plt.figure()

panel = f.add_subplot(111)
plt.title("Stationary Target in Front - Prey Post-Evolution")
plt.xlabel("Time Step")
plt.ylabel("Length of Ray Sensor")
plt.plot(parents.p[0].D)

plt.show()

parents.p[0].Start_Evaluation(envs.envs[1], pp = False, pb = True)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[2], pp = False, pb = True)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[3], pp = False, pb = True)
parents.p[0].Compute_Fitness()

print("EVOLVED PREY GENOME FOR STATIONARY LIGHT SOURCE")
print(c.evolvedGenomePrey)

f = plt.figure()

panel = f.add_subplot(111)
plt.title("Evolving Fitness for Prey with Stationary Objects")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.plot(fitness)

plt.show()
"""
c.D = .1
c.red = 1
c.blue = 0
c.preyX = 0

#######################################################################################################
print ("EVOLVING PREDATOR FOR MOVING LIGHT SOURCE")
fitness = []
envs = MOVING_ENVIRONMENTS()

parents = PREDATOR_POPULATION(c.popSize)

parents.Initialize()

parents.Evaluate(envs, pp=False, pb=True)
print (0, end = " ")
parents.Print()


for g in range(1, c.numGens+1):
    children = PREDATOR_POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp = False, pb =True)
    print(g, end = " ")
    children.Print()
    
    parents.ReplaceWith(children)
    fitness.append(parents.p[0].fitness)
    
#c.evolvedGenomePredator = parents.p[0].genome    

parents.p[0].Start_Evaluation(envs.envs[0], pp = True, pb = False)
parents.p[0].Compute_Fitness()
"""
parents.p[0].Start_Evaluation(envs.envs[1], pp = True, pb = False)
parents.p[0].Compute_Fitness()
True
parents.p[0].Start_Evaluation(envs.envs[2], pp = True, pb = False)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[3], pp = True, pb = False)
parents.p[0].Compute_Fitness()

print("EVOLVED PREDATOR GENOME FOR MOVING LIGHT SOURCE")
print(c.evolvedGenomePredator)
"""
f = plt.figure()

panel = f.add_subplot(111)
plt.title("Evolving Fitness for Predator with Moving Objects")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.plot(fitness)

plt.show()
c.D = .01
c.red = 0
c.blue = 1
c.preyX = 0
#######################################################################################################
print("EVOLVING PREY FOR MOVING LIGHT SOURCE")
fitness = []
envs = MOVING_ENVIRONMENTS()

parents = PREY_POPULATION(c.popSize)

parents.Initialize()
parents.Evaluate(envs, pp = False, pb = True)
print(0, end = " ")
parents.Print()

for g in range(1, c.numGens+1):
    children = PREY_POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp = False, pb =True)
    print(g, end = " ")
    children.Print()
    
    parents.ReplaceWith(children)
    fitness.append(parents.p[0].fitness)


#c.evolvedGenomePrey = parents.p[0].genome    
"""  
parents.p[0].Start_Evaluation(envs.envs[0], pp = True, pb = False)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[1], pp = True, pb = False)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[2], pp = True, pb = False)
parents.p[0].Compute_Fitness()

parents.p[0].Start_Evaluation(envs.envs[3], pp = True, pb = False)
parents.p[0].Compute_Fitness()

print("EVOLVED PREY GENOME FOR MOVING LIGHT SOURCE")
print(c.evolvedGenomePrey)
"""

f = plt.figure()

panel = f.add_subplot(111)
plt.title("Evolving Fitness for Prey with Moving Objects")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.plot(fitness)

plt.show()
#######################################################################################################
print("EVOLVING COMBINED PAIR")
fitness = []
parents = COMBINED_POPULATION(c.popSize)

parents.Initialize()
parents.Evaluate(pp = False, pb = True)
print(0, end = " ")
parents.Print()

for g in range(1, c.numGens+1):
    children = COMBINED_POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(pp = False, pb =True)
    print(g, end = " ")
    children.Print()
    
    parents.ReplaceWith(children)
    fitness.append(parents.p[0].fitness)
    
parents.p[0].Start_Evaluation( pp = True, pb = False)
parents.p[0].Compute_Fitness()

f = plt.figure()

panel = f.add_subplot(111)
plt.title("Evolving Fitness for Combined Pair")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.plot(fitness)

plt.show()
