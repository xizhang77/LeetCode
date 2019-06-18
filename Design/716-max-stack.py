# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/max-stack/
'''

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            temp = x
        else:
            temp = max(self.stack[-1][1], x )
        self.stack.append( (x, temp) )

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        ans = self.stack[-1][1]
        temp = []
        while self.stack[-1][0] != ans:
            temp.append( self.stack.pop()[0] )
        self.stack.pop()
        while temp:
            self.push( temp.pop() )
        
        return ans

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()