import copy
from random import randint
import constants as c
from movingEnvironment import MOVING_ENVIRONMENT  

class MOVING_ENVIRONMENTS:
    
    def __init__(self):
        
        self.envs = {}
        
        for e in range( 0 , c.numEnvs ):
            self.envs[e] = MOVING_ENVIRONMENT(e)

       