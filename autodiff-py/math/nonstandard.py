import numpy as np

class NonstandardBase: # used for type hints
    
    def __init__(self, std: float, inf: float):
        
        if not isinstance(std, float):
            raise TypeError("Standard part of Nonstandard number must be of type float.")
        if not isinstance(inf, float):
            raise TypeError("Infinitesimal part of Nonstandard number must be of type float.")
        self.std = std
        self.inf = inf

class Nonstandard(NonstandardBase):
        
    def __str__(self) -> str:
        
        if self.inf == 0.0:
            return str(self.std)
        elif self.std == 0.0:
            return str(self.inf) + "e"
        else:
            return str(self.std) + "+" + str(self.inf) + "e"
        
    def __repr__(self) -> str:
        return self.__str__()
    
    def __add__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Nonstandard numbers can only be summed with other Nonstandard numbers.")
        return Nonstandard(self.std + other.std, self.inf + other.inf)
    
    def __sub__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Nonstandard numbers can only be subtracted with other Nonstandard numbers.")
        return Nonstandard(self.std - other.std, self.inf - other.inf)
    
    def __mul__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Nonstandard numbers can only be multiplied with other Nonstandard numbers.")
        return Nonstandard(self.std*other.std, self.std*other.inf + self.inf*other.std)
    
    def __truediv__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Nonstandard numbers can only be divided by other Nonstandard numbers.")
        if other.std == 0.0:
            raise ValueError("Cannot divide by Nonstandard number with standard part equal to zero.")
        return Nonstandard(self.std/other.std, (self.inf*other.std - self.std*other.inf)/(other.std*other.std))
    
    def __pow__(self, other: float) -> NonstandardBase:
        
        if not isinstance(other, float):
            raise TypeError("Exponent for Nonstandard numbers must be of type float.")
        if self.std == 0.0:
            raise ValueError("Cannot take power of Nonstandard number with zero standard part.")
        if other == 0.0:
            return Nonstandard(1.0, 0.0)
        else:
            return Nonstandard(self.std**other, other*self.std**(other-1)*self.inf)
    
    def __abs__(self) -> NonstandardBase:
        if self.std == 0.0:
            raise ValueError("Cannot take absolute value of Nonstandard number with zero standard part.")
        return Nonstandard(abs(self.std), self.inf*np.sign(self.std))
    
    def __eq__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            return False
        return (self.std == other.std) & (self.inf == other.inf)
    
    def __lt__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Can only compare Nonstandard numbers with other Nonstandard numbers.")
        if (self.std < other.std):
            return True
        elif (self.std == other.std):
            return (self.inf < other.inf)
        else:
            return False
    
    def __le__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Can only compare Nonstandard numbers with other Nonstandard numbers.")
        if (self.std < other.std):
            return True
        elif (self.std == other.std):
            return (self.inf <= other.inf)
        else:
            return False
        
    def __gt__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Can only compare Nonstandard numbers with other Nonstandard numbers.")
        if (self.std > other.std):
            return True
        elif (self.std == other.std):
            return (self.inf > other.inf)
        else:
            return False
    
    def __ge__(self, other: NonstandardBase) -> NonstandardBase:
        
        if not isinstance(other, Nonstandard):
            raise TypeError("Can only compare Nonstandard numbers with other Nonstandard numbers.")
        if (self.std > other.std):
            return True
        elif (self.std == other.std):
            return (self.inf >= other.inf)
        else:
            return False