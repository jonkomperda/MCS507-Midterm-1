class contFrac():
    """Calculates the continued fraction representation of x"""
    def __init__(self, x, n):
        self.x = x
        self.n = n
        self.output = []
        
    def step(self):
        """takes a step in the continued fraction representation"""
        out = self.x // self.n # // is integer division in python 2.2+
        self.n, self.x = self.x-self.n*out, self.n
        self.output.append(out)
        return out
    
    def next(self):
        """this is our iterator"""
        if self.n:
            print self.step()
        else:
            raise StopIteration("You have exceeded the number of terms")
    
    def __str__(self):
        """string representation of our data"""
        return str(self.output)
    
if __name__ == '__main__':
    from math import pi
    a = contFrac(pi,1)
    a.next()
    a.next()
    a.next()
    a.next()
    a.next()
