# -*- coding: utf-8 -*-

'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return matrix
        
        m, n = len(matrix), len( matrix[0] )
        
        curr = []        
        ans = [ [-1]*n for _ in range( m ) ]
        for i in range( m ):
            for j in range( n ):
                if matrix[i][j] == 0:
                    curr.append( [i,j] )
                    ans[i][j] = 0
        
        direct = [[0,1], [1,0], [-1,0], [0,-1] ]
        level = 1
        while curr:
            nxt = []
            for point in curr:
                for d in direct:
                    ii, jj = point[0] + d[0], point[1] + d[1]
                    if 0 <= ii < m and 0 <= jj < n and ans[ii][jj] == -1:
                        nxt.append( [ii, jj] )
                        ans[ii][jj] = level
            curr = nxt
            level += 1
        
        return ans