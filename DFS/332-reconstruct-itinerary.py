# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/reconstruct-itinerary/
'''


class Solution(object):
    def dfs(self, hashmap, n, start, path):
        if self.ans:
            return
        if len(path) == n:
            self.ans = path
            return
        if start not in hashmap:
            return

        for i in range( len( hashmap[ start ] )):
            stop = hashmap[ start ].pop( i )
            self.dfs( hashmap, n, stop, path + [ stop ] )
            hashmap[ start ].insert( i, stop )
            
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        hashmap = {}
        
        for t in tickets:
            start, end = t
            if start not in hashmap:
                hashmap[ start ] = [ end ]
            else:
                hashmap[ start ] += [ end ]
                
        for key in hashmap:
            hashmap[ key ] = sorted( hashmap[ key ] )
        
        self.ans = []
        self.dfs( hashmap, len(tickets) + 1, 'JFK', [ 'JFK' ] )
            
        return self.ans