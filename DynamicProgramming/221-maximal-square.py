# -*- coding: utf-8 -*-

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

'''
这道题期初想仿照LeetCode #85 maximal rectangle的做法，但是失败了。我觉得应该可以再抢救一下… 
'''

# Solution 1: DP
# Time and Space: O(m*n)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [ [0]*n for _ in range(m) ]
        
        
        for i in range(m):
            dp[i][0] = int( matrix[i][0] )
        
        for j in range(n):
            dp[0][j] = int( matrix[0][j] )
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        
        return max( max(row) for row in dp ) ** 2