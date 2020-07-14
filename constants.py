import numpy as np

preyX = 0

D = .1

L = 0.1

R = L/5

wR = .025
#timesteps
evalTime = 1500

popSize = 10

numGens = 1

numEnvs = 4

evolvedGenomePrey = np.random.random(size = (5,4))*2 - 1 

evolvedGenomePredator = np.random.random(size = (5,4))*2 - 1 

red = 1

blue = 0

