# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/max-points-on-a-line/

Function gcd and frac are used only for one test case: [[0,0],[94911151,94911150],[94911152,94911151]]
'''


# Time: O(n^2); Space: O( n )
class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def frac(self, x, y):
        g = self.gcd(x,y)
        return x//g, y//g
    
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        
        if n < 3:
            return n
        
        ans = 0
        
        for i in range( n ):
            hashMap = {'inf': 0 }
            samePoint = 1
            for j in range( n ):
                if i == j:
                    continue
                if points[i] == points[j]:
                    samePoint += 1
                else:
                    if points[i][0] == points[j][0]:
                        hashMap[ 'inf' ] += 1
                    else:
                        slop = self.frac(points[i][1] - points[j][1], points[i][0] - points[j][0])
                        if slop not in hashMap:
                            hashMap[ slop ] = 1
                        else:
                            hashMap[ slop ] += 1
            ans = max( ans, max(hashMap.values()) + samePoint )
        
        return ans