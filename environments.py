import copy
from random import randint
import constants as c
from envrironment import ENVIRONMENT  

class EVIRONMENTS:
    
    def __init__(self):
        
        self.envs = {}
        
        for e in range( 0 , c.numEnvs ):
            self.envs[e] = ENVIRONMENT(e)

       