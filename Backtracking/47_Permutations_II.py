# -*- coding: utf-8 -*-

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

# Time: O(2^n); Space: O(n)
class Solution(object):
    def dfs(self, nums, path, ans):
        if not nums:
            ans.append( path )
            return 
        
        i = 0
        while i < len(nums):
            self.dfs( nums[:i] + nums[i+1:], path + [nums[i]], ans )
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            i += 1
            
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( sorted(nums), [], ans )
        
        return ans