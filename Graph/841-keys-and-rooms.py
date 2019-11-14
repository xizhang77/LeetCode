# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/keys-and-rooms/
'''

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len( rooms )
        
        visited = [ False ]*n        
        curr = set( [0] )
        
        while curr:
            nxt = set()
            for i in curr:
                visited[ i ] = True
                for key in rooms[i]:
                    if not visited[ key ]:
                        nxt.add( key )
            curr = nxt
        
        return visited == [True]*n