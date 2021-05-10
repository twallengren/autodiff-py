import infinitesimal as inf
import nonstandard as ns

class Real:
    
    def __init__(self, value=1.0):
        if not isinstance(value, float):
            raise TypeError("Real value must be of type float.")
        self.value = value
        
    def __str__(self):
        return "RE: " + str(self.value)
    
    def __add__(self, other):
        
        if isinstance(other, Real):
            return Real(self.value + other.value)
        elif isinstance(other, inf.Infinitesimal):
            return ns.Nonstandard(self, other)
        else:
            raise TypeError("Addition with Real undefined for " + str(type(other)))
    
    def __mul__(self, other):
        
        if isinstance(other, inf.Infinitesimal):
            return inf.Infinitesimal(self.value*other.value)
        elif isinstance(other, Real):
            return Real(self.value*other.value)
        else:
            raise TypeError("Multiplication with Real undefined for " + str(type(other)))