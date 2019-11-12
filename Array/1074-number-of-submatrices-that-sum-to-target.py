# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
'''

from collections import defaultdict

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        
        for i in range( m ):
            for j in range( 1, n ):
                matrix[i][j] += matrix[i][j-1]
        
        ans = 0
        
        for i in range( n ):
            for j in range( i, n ):
                hashmap = defaultdict( int )
                hashmap[ 0 ] += 1
                
                currsum = 0
                for k in range( m ):
                    if i == 0:
                        currsum += matrix[k][j]
                    else:
                        currsum += matrix[k][j] - matrix[k][i-1]
                    if currsum - target in hashmap:
                        ans += hashmap[ currsum - target ]
                    hashmap[ currsum ] += 1
        return ans
                    