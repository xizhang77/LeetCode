# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/network-delay-time/
'''

from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edges = defaultdict( list )
        for time in times:
            u, v, w = time
            edges[u].append( [w, v] )
        
        if K not in edges:
            return -1
        
        dist = [float('inf')]*(N+1)
        dist[ 0 ] = dist[ K ] = 0
        for w, v in edges[ K ]:
            dist[ v ] = w
        
        points = range(1, K) + range( K+1, N+1 )
        
        while points:
            minimum, idx = float('inf'), 0
            for i in range( len(points) ):
                if dist[ points[i] ] < minimum:
                    minimum, idx = dist[ points[i] ], i
            
            pivot = points[ idx ]
            points.pop( idx )
            
            if pivot in edges:
                for w, v in edges[ pivot ]:
                    if dist[ v ] > minimum + w:
                        dist[ v ] = w + minimum
            
        ans = max( dist )
        if ans == float('inf'):
            return -1
        return ans
            