# -*- coding: utf-8 -*-
'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

# Solution 1: Time & Space: O(n^2)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        matrix = [ [ None for _ in range(n) ] for _ in range(n) ]
        
        direct = [ [0, 1], [1, 0], [0, -1], [-1, 0] ]
        
        flag = 0
        i, j = 0, -1
        num = 1
        while num <= n**2:
            flag = flag%4
            i += direct[flag][0]
            j += direct[flag][1]
            while 0 <= i < n and 0 <= j < n and matrix[i][j] == None:
                matrix[i][j] = num
                i += direct[flag][0]
                j += direct[flag][1]
                num += 1
            i -= direct[flag][0]
            j -= direct[flag][1]
            flag += 1

        return matrix

# Much clearer verison, same complexity
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        matrix = [ [ 0 for _ in range(n)] for _ in range(n) ]
        
        
        i, j = 0, 0
        di, dj = 0, 1
        
        for num in range(1, n*n+1):
            matrix[i][j] = num
            if matrix[ (i+di)%n ][ (j+dj)%n ]:
                di, dj = dj, -di
            i += di
            j += dj
        
        return matrix