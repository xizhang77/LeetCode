# -*- coding: utf-8 -*-

'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

# Time & Space: O(n^2)

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [ [1], [1,1] ]
        
        if numRows <= 2:
            return dp[: numRows]
                
        for i in range(2, numRows):
            temp = []
            for j in range( len(dp[-1]) - 1):
                temp.append( dp[-1][j] + dp[-1][j+1] )
            dp.append( [1] + temp + [1] )
        
        return dp