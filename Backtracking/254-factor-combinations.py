# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/factor-combinations/
'''


from math import sqrt
class Solution(object):
    def solver(self, start, n):
        if n < 2:
            return []
        ans = []
        for i in range( start, int(sqrt( n )) + 1 ):
            if n%i == 0:
                ans.append( [i, n/i] )
                res = self.solver( i, n/i )
                for val in res:
                    ans.append( [i] + val )
        return ans
    
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.solver( 2, n )