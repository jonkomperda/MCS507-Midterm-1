class stirling():
    """docstring for stirling"""
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.dict = {(0,0):1}
        
    
    def c(self, n, k):
        """docstring for compute"""
        if (n==0) and (k==0):
            return 1
        if (n <= 0) or (k <= 0):
            return 0
        else:
            ans = - (n-1)*self.c(n-1,k) + self.c(n-1,k-1)
            return ans

if __name__ == '__main__':
    a = stirling(3,2)
    print a.c(5,5)