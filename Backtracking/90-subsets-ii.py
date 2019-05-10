# -*- coding: utf-8 -*-

'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

# Reminder: subset is not subarray...
# Time: O(2^n)

class Solution(object):
    def dfs(self, nums, path, ans):
        ans.append( path )
        if not nums:
            return
        
        i = 0
        while i < len(nums):
            self.dfs( nums[i+1:], path + [ nums[i] ], ans )
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
            
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( sorted(nums), [], ans )
        
        return ans