import real as re
import nonstandard as ns

class Infinitesimal:
    
    def __init__(self, value=1.0):
        if not isinstance(value, float):
            raise TypeError("Infinitesimal value must be of type float.")
        self.value = value
        
    def __str__(self):
        return "INF: " + str(self.value) + "e"
    
    def __add__(self, other):
        
        if isinstance(other, Infinitesimal):
            return Infinitesimal(self.value + other.value)
        elif isinstance(other, re.Real):
            return ns.Nonstandard(other, self)
        else:
            raise TypeError("Addition with Infinitesimal undefined for " + str(type(other)))
    
    def __mul__(self, other):
        
        if isinstance(other, Infinitesimal):
            return re.Real(0.0)
        elif isinstance(other, re.Real):
            return Infinitesimal(self.value*other.value)
        else:
            raise TypeError("Multiplication with Infinitesimal undefined for " + str(type(other)))
    