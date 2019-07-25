# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/set-matrix-zeroes/
'''

# Time: O(mn); Space: O(n)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        col = set()
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            flag = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    flag = 1
                    col.add(j)
            if flag:
                for j in range(n):
                    matrix[i][j] = 0

        
        for j in col:
            for i in range(m):
                matrix[i][j] = 0


# Time: O(mn); Space: O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -float('inf')
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -float('inf')
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -float('inf'):
                    matrix[i][j] = 0