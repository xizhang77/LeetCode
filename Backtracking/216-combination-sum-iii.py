# -*- coding: utf-8 -*-

'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution(object):
    def dfs(self, ans, path, k, n, start):
        if n < 0:
            return
        if n == 0 and len(path) == k:
            ans.append( path )
            return
        for i in range( start, 10 ):
            self.dfs( ans, path + [i], k, n - i, i + 1 )
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        
        if n/k > 9:
            return ans
        
        for i in range(1, 10):
            if i > n/k:
                break
            
            self.dfs( ans, [ i ], k, n - i , i + 1 )
            
        return ans