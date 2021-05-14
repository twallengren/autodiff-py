import numpy as np
from nonstandard import Nonstandard

def sin(x: Nonstandard) -> Nonstandard:
    
    if not isinstance(x, Nonstandard):
        raise TypeError("Argument of sin must be of type Nonstandard.")
    return Nonstandard(np.sin(x.std), x.inf*np.cos(x.std))

def cos(x: Nonstandard) -> Nonstandard:
    
    if not isinstance(x, Nonstandard):
        raise TypeError("Argument of cos must be of type Nonstandard.")
    return Nonstandard(np.cos(x.std), -x.inf*np.sin(x.std))