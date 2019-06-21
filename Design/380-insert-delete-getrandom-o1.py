# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array, self.map = [], {}
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.map[ val ] = self.length
            self.array.append( val )
            self.length += 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            new_val = self.array[-1]
            if val != new_val:
                self.array[ self.map[val] ] = new_val
                self.map[ new_val ] = self.map[ val ]
            self.array.pop()
            del self.map[ val ]
            self.length -= 1
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.length - 1)
        return self.array[ idx ]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()