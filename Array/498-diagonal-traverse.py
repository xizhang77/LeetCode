# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/diagonal-traverse/
'''

# Time: O(m*n); Space: O(1)
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """        
        ans = []
        
        if not matrix or not matrix[0]:
            return ans
        
        m, n = len(matrix), len(matrix[0])
        
        p = q = 0
        flag = 1
        while 0 <= p + q <= m+n-2:
            while 0 <= p < m and 0 <= q < n:
                ans.append( matrix[p][q] )
                prev_p, prev_q = p, q
                if flag:
                    p -= 1
                    q += 1
                else:
                    p += 1
                    q -= 1
            p, q = prev_p, prev_q
            if flag:
                if q + 1 < n:
                    q += 1
                else:
                    p += 1
            else:
                if p + 1 < m:
                    p += 1
                else:
                    q += 1
            flag = 1 - flag

        return ans