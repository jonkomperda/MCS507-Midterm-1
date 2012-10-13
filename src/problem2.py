class stirling():
    """Upon initialization we have the dictionary with the 0,0 condition created."""
    def __init__(self, n, k):
        self.dict = {(0,0):1} #start with the initial condition (saves an if statement)
        self.answer = self.c(n,k)
        
    
    def c(self, n, k):
        """Computes stirling numbers either recursively or by looking up in dictionary"""
        if (n,k) in self.dict.keys():
            #print 'using dict for: '+str((n,k)) #checks to see if we used the dictionary or not
            return self.dict[(n,k)]
        elif n<=0 or k<=0:
            return 0
        else:
            ans = - (n-1)*self.c(n-1,k) + self.c(n-1,k-1)
            self.dict[(n,k)] = ans
            return ans
    
    def __str__(self):
        """string representation of our data"""
        return 'Computed answer: '+str(self.answer)+'\nDictionary Values: \n'+str(self.dict)

if __name__ == '__main__':
    a = stirling(5,2)
    print a