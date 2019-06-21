# -*- coding: utf-8 -*-

'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.stack = []
        self.n = size
        self.length = 0
        self.sum = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        
        if self.length < self.n:
            self.stack.append( val )
            self.length += 1
            self.sum += val
            return self.sum/self.length
        
        else:
            remove = self.stack.pop(0)
            self.stack.append( val )
            self.sum = self.sum - remove + val
            return self.sum/self.length
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)