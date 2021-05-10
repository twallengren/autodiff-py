import real as re
import infinitesimal as inf

class Nonstandard:
    
    def __init__(self, real, infinitesimal):
        
        if not isinstance(real, re.Real):
            raise TypeError("Real part of Nonstandard number must be of type Real.")
        if not isinstance(infinitesimal, inf.Infinitesimal):
            raise TypeError("Infinitesimal part of Nonstandard number must be of type Infinitesimal.")
        
        self.re = real
        self.inf = infinitesimal
        
    def __str__(self):
        return "NS: " + str(self.re.value) + "+" + str(self.inf.value) + "e"
    
    def __add__(self, other):
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Nonstandard numbers can only be summed with other Nonstandard numbers.")
        return Nonstandard(self.re + other.re, self.inf + other.inf)
    
    def __mul__(self, other):
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Nonstandard numbers can only be multiplied with other Nonstandard numbers.")
        return Nonstandard(self.re*other.re, self.re*other.inf + self.inf*other.re)