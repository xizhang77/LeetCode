# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/lfu-cache/
'''

from collections import defaultdict

class Node(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None
        
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.freq = defaultdict( list )
        self.min = float('inf')
        self.len = 0
        self.capacity = capacity
    
    def remove(self, level, node):
        # Remove from level
        if self.freq[level][0] == self.freq[level][1] == node:
            del self.freq[ level ]
            if self.min == level:
                self.min = level + 1 if self.map else float('inf')
                
        elif self.freq[level][0] == node:
            newhead = node.next
            self.freq[level][0] = newhead
            if newhead:
                newhead.prev = None
                
        elif self.freq[level][1] == node:
            newtail = node.prev
            self.freq[level][1] = newtail
            if newtail:
                newtail.next = None
        else:
            front, end = node.prev, node.next
            front.next = end
            end.prev = front
        
    def insert(self, level, node):
        # Insert in the new level
        if level not in self.freq:
            self.freq[ level ] = [node, node]
        else:
            tail = self.freq[ level ][ 1 ]
            tail.next = node
            node.prev = tail
            self.freq[ level ][ 1 ] = node
            
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            val, node, level = self.map[ key ]
            self.remove( level, node )
            self.insert( level + 1, node)
            self.map[ key ][ -1 ] += 1 
            # print self.map, self.freq
            return val
        
        return -1
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print self.map, self.freq, self.min
        if self.capacity == 0:
            return
        
        if key in self.map:
            node, level = self.map[ key ][1:]
            self.remove( level, node )
            self.insert( level + 1, node)
            self.map[ key ][ -1 ] += 1
            self.map[ key ][ 0 ] = value
        else:
            if self.len == self.capacity:
                node = self.freq[ self.min ][ 0 ]
                rm_key = node.val
                del self.map[ rm_key ]
                self.remove( self.min, node )
                self.len -= 1
                
            node = Node( key )
            self.map[ key ] = [ value, node, 1 ]
            self.insert( 1, node )
            self.min = min(self.min, 1 )
            self.len += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)