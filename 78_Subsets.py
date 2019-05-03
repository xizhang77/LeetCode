# -*- coding: utf-8 -*-

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution(object):
    def dfs(self, nums, path, ans):
        ans.append( path )
        
        if not nums:
            return 
        
        for i in range( len(nums) ):
            self.dfs( nums[i+1:], path+[ nums[i] ], ans)
            
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( nums, [], ans )
        
        return ans