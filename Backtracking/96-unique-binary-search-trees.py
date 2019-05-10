# -*- coding: utf-8 -*-

'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Solution 1 [DFS + DP]
# Can also be solved as a pure math question

class Solution(object):
    def dfs(self, n, count):
        if n == 0 or n == 1:
            return 1
        if count[n - 1]:
            return count[n - 1]
        
        temp = 0
        for i in range( n ):
            temp += self.dfs( i, count ) * self.dfs( n - i - 1, count )
        
        count[ n - 1 ] = temp
        
        return temp
        
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [ 0 ] * n
        
        return self.dfs( n, count )