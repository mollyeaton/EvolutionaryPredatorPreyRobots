import copy
from random import randint
import constants as c
from stationaryEnvironment import STATIONARY_ENVIRONMENT  

class STATIONARY_EVIRONMENTS:
    
    def __init__(self):
        
        self.envs = {}
        
        for e in range( 0 , c.numEnvs ):
            self.envs[e] = STATIONARY_ENVIRONMENT(e)

       