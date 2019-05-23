# -*- coding: utf-8 -*-

'''
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

# Solution 1
# Space: O(m*n); Time: O(m*m*n) [ Runtime: 644 ms, faster than 10.15% ]
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        ans = 0
        m, n = len(matrix), len(matrix[0])
        
        dp = [ [float('inf') for _ in range(n)] for _ in range(m) ]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j - 1 >= 0 and dp[i][j-1] != float('inf'):
                        dp[i][j] = min(dp[i][j-1], j)
                    else:
                        dp[i][j] = j
                    ans = max( ans, j - dp[i][j] + 1 )
                    if i - 1 >= 0 and dp[i-1][j] != float('inf'):
                        temp = []
                        row = i
                        while row >= 0 and dp[row][j] != float('inf'):
                            temp.append( dp[row][j] )
                            row -= 1
                            ans = max( ans, (i - row)*(j - max(temp) + 1) )
        return ans



# Solution 2: Stack + DP, generated based on Leetcode #74
# Time: O(m*n); Space: O(n) [Runtime: 176 ms, faster than 62.68% ]
class Solution(object):
    def maxArea(self, height):
        height.append( 0 )
        stack = [ -1 ]
        ans = 0
        
        for i in range( len(height) ):
            while height[i] < height[ stack[-1] ]:
                idx = stack.pop()
                ans = max(ans, height[ idx ] *(i - stack[-1] - 1))
            stack.append(i)
        
        return ans
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [ 0 for i in range(n) ]
        
        ans = 0
        
        for i in range(m):
            temp = []
            for j in range(n):
                if matrix[i][j] == '0':
                    temp.append(0)
                else:
                    temp.append( dp[j] + 1 )

            ans = max( ans, self.maxArea( temp ) )
            dp = temp
        
        return ans