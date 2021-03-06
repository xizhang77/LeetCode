# -*- coding: utf-8 -*-

'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Time Complexity: O(m+n); Space: O(m)
# Where n is the number of nodes and m is the levels


# Solution 1: BFS
from collections import defaultdict

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        hashmap = defaultdict( int )
        
        current = nestedList
        level = 1
        while current:
            nextlevel = []
            for val in current:
                if val.isInteger():
                    hashmap[ level ] += val.getInteger()
                else:
                    nextlevel += val.getList()
            level += 1
            current = nextlevel
        
        ans = 0
        for key in hashmap:
            ans += (level - key) * hashmap[key]
        return ans

# Solution 2: DFS
from collections import defaultdict

class Solution(object):
    def dfs(self, level, num):
        if not num:
            return
        self.depth = max( self.depth, level )
        if not num.isInteger():
            nested = num.getList()
            for newnum in nested:
                self.dfs( level+1, newnum )
        else:
            self.map[ level ] += num.getInteger()
        
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.map = defaultdict( int )
        self.depth = 1
        for num in nestedList:
            self.dfs( 1, num )
        
        ans = 0
        for key in self.map:
            ans += (self.depth - key + 1)*self.map[ key ]
        
        return ans