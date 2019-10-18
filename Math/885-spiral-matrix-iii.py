# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/spiral-matrix-iii/
'''

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        i, j = r0, c0
        
        sign = 1
        step = 1
        ans = [ [r0,c0] ]
        
        while len(ans) < R*C:
            for _ in range(step):
                j += sign
                if 0 <= i < R and 0 <= j < C:
                    ans.append( [i, j] )
            for _ in range(step):
                i += sign
                if 0 <= i < R and 0 <= j < C:
                    ans.append( [i, j] )
            
            sign *= -1
            step += 1
        
        return ans