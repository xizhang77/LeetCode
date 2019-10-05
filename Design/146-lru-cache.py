# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/lru-cache/
'''

# Solution 2: OrderedDict

# Solution 1: LinkedList + HashTable
class Node(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.head = None
        self.tail = None
        self.len = 0
        self.capacity = capacity
        
    def update(self, node):
        if node == self.tail:
            return
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        else:
            before, after = node.prev, node.next
            before.next = after
            after.prev = before
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            val, node = self.map[ key ]
            self.update( node )
            return val
        
        return -1
    
    def insert(self, node):
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[ key ][ 1 ]
            self.map[ key ][0] = value
            self.update( node )
        else:
            if self.len == self.capacity:
                p = self.head
                rm_key = p.val
                del self.map[ rm_key ]
                self.head = p.next
                if self.head:
                    self.head.prev = None
                self.len -= 1
            
            newnode = Node( key )
            
            self.map[ key ] = [ value, newnode ]
            self.len += 1
            
            self.insert( newnode )
            
            
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)