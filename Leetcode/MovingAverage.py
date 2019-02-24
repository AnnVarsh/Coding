class MovingAverage:

    def __init__(self, size: 'int'):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.size = size
        self.index = 0

    def next(self, val: 'int') -> 'float':

        if len(self.q) < self.size:
            self.q.append(val)
            self.index += 1
            return sum(self.q) /float(len(self.q))
        else:
            self.index = self.index % self.size
            self.q[self.index] = val
            self.index += 1
            return sum(self.q) /float(len(self.q))
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)