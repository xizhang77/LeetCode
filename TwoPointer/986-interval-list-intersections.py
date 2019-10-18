# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/interval-list-intersections/
'''

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        
        i = j = 0
        m, n = len(A), len(B)
        
        while i < m and j < n:
            if A[i][1] < B[j][0]:
                i += 1
            elif A[i][0] > B[j][1]:
                j += 1
            else:
                ans.append( [max(A[i][0], B[j][0]), min(A[i][1], B[j][1])] )
                if A[i][1] > B[j][1]:
                    j += 1
                elif A[i][1] < B[j][1]:
                    i += 1
                else:
                    i += 1
                    j += 1
        
        return ans
                    