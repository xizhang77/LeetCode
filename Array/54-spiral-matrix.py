# -*- coding: utf-8 -*-

'''
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


# Time: O(m*n); Space: O(1)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        
        if not matrix or not matrix[0]:
            return ans
        
        m, n = len(matrix), len(matrix[0])
        
        direct = [ [0,1], [1,0], [0,-1], [-1,0] ]
        
        flag = 0
        i = j = 0
        while len(ans) < m*n:
            ans.append( matrix[i][j] )
            matrix[i][j] = None
            ii, jj = i + direct[flag][0], j + direct[flag][1] 
            if ii == m or jj == n or matrix[ii][jj] == None:
                flag = (flag + 1)%4
                i += direct[flag][0]
                j += direct[flag][1] 
            else:
                i, j = ii, jj 
        
        return ans