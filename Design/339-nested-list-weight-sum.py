# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/nested-list-weight-sum/
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

# Solution 1: Recursively
from collections import defaultdict
class Solution(object):
    def dfs(self, num, level):
        if not num:
            return
        if num.isInteger():
            self.table[ level ] += num.getInteger()
        else:
            temp = num.getList()
            for newnum in temp:
                self.dfs( newnum, level + 1 )
        
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.table = defaultdict( int )

        for val in nestedList:
            self.dfs( val, 1 )
        
        ans = 0
        for key in self.table:
            ans += key*self.table[ key ]
        
        return ans

# Solution 2: Interactively
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth, ans = 1, 0
        
        while nestedList:
            num, nextList = 0, []
            for i in nestedList:
                if i.isInteger():
                    num += i.getInteger()
                else:
                    nextList += i.getList()
            ans += depth*num
            depth += 1
            nestedList = nextList
        
        return ans
         