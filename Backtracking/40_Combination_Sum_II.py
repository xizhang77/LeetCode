# -*- coding: utf-8 -*-

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''

# Time: O( 2^n ) ; Space: O( n )
# n: length of candidates
# reference: https://github.com/Deadbeef-ECE/Interview/blob/master/Leetcode/BackTracking/040_Combination_Sum_II.java
class Solution(object):
    def dfs(self, nums, target, path, ans ):
        if target == 0:
            ans.append( path )
            return
        
        i= 0
        while i < len(nums):
            if target - nums[i] >= 0:
                self.dfs( nums[i+1:], target - nums[i], path + [ nums[i] ], ans )
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
                
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( sorted(candidates), target, [], ans )
        
        return ans