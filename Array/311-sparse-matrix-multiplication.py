# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/sparse-matrix-multiplication/
'''

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(B[0])
        
        res = [ [0]*n for _ in range(m) ]
        
        for i in range(m):
            for k in range( len(A[0]) ):
                if A[i][k] != 0:
                    for j in range( n ):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k]*B[k][j]
        
        
        return res