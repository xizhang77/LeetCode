# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/rectangle-area/
'''


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1, area2 = (C-A)*(D-B), (G-E)*(H-F)
        
        x, y = min(C, G) - max(A, E), min(D, H) - max(B, F)
        
        if x > 0 and y > 0:
            return area1 + area2 - x * y
        else:
            return area1 + area2