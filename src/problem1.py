class contFrac():
    """Calculates the continued fraction representation of x"""
    def __init__(self, x, n=1):
        self.x = x
        self.n = n
        self.output = []
        
    def step(self):
        """takes a step in the continued fraction representation"""
        out = self.x // self.n # // is integer division in python 2.2+
        self.n, self.x = self.x-self.n*out, self.n
        self.output.append(int(out))
        return int(out)
    
    def next(self):
        """this is our iterator"""
        if self.n:
            return self.step()
        else:
            raise StopIteration("You have exceeded the number of terms")
    
    def run(self):
        """
        Runs the continued fraction until we're out of digits
        Not part of the assignment, but eases testing since you dont need to take
        individual steps. Automatically stops when out of digits
        """
        while self.n:
            self.step()
    
    def __str__(self):
        """string representation of our data"""
        return str(self.output)
    
if __name__ == '__main__':
    from math import pi
    print 'First we do the example presented in the assignment:'
    print 'Calculating continued fraction of 2.25'
    a = contFrac(2.25)
    b = [a.next() for x in range(2)]
    print b
    print 'Calculating continued fraction of 9/4'
    e = contFrac(9,4)
    f = [e.next() for x in range(2)]
    print f
    
    print '\nWe now calculate the continued fraction of pi for 10 digits for a benchmark'
    c = contFrac(pi)
    d = [c.next() for x in range(10)]
    print 'Computed Value: ' + str(d)
    print 'Bench Value:    [3, 7, 15, 1, 292, 1, 1, 1, 2, 1]'
    
    print '\nNow show that the iterator raises an error if you go too far...'
    a.next()
    