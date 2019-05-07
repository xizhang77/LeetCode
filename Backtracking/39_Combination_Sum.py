# -*- coding: utf-8 -*-

'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution(object):
    def dfs(self, nums, target, path, ans):
        if target == 0:
            ans.append( path )
            return
        
        for i in range( len(nums) ):
            if target - nums[i] >= 0:
                self.dfs( nums[i:], target - nums[i], path + [nums[i]], ans )
                
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( candidates, target, [], ans)
        
        return ans