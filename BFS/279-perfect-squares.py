# -*- coding: utf-8 -*-

'''
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

# Solution 1 [DFS, LTE, 502 / 588 test cases passed.]
from math import sqrt
class Solution(object):
    def dfs(self, n, count):
        if self.ans < count:
            return
        if n == 0:
            self.ans = count
            return
        
        for i in range( int(sqrt(n)), 0, -1 ):
                self.dfs( n - i * i, count + 1 )
                
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = n
        self.dfs( n, 0 )
        
        return self.ans

# Solution 2: BFS
from math import sqrt
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        
        stack = [ n ]
        
        while stack:
            ans += 1
            
            nextLevel = []
            for num in stack:
                for i in range( int(sqrt(num)), 0, -1 ):
                    nextLevel.append( num - i*i )
                    if num - i * i == 0:
                        return ans
            stack = nextLevel

# Solution 3: DP [I don't think it's a wise choice to use DP here... ]