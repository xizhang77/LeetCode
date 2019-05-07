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
# 参考：https://github.com/Deadbeef-ECE/Interview/blob/master/Leetcode/BackTracking/039_Combination_Sum.java

# Time: O( k * 2^n')
# 此题可以转换成 Combination Sum II, 如何做呢, 举个栗子:
# int[] arr = {2, 3, 4, 5, 6}, target = 10; 我们知道此题中,每个元素可以重复用, 
# 其实, 如果把 arr 变成 {2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6}, 然
# 后每个元素只能用一次, 就变成了Combination Sum II的要求了. 
# 我们再看新数组, 元素多了很多, 多了多少? 
# 那就是数组中所有小于等于target的元素E增加了ceil(target/E)个, 然后就可以用
# Combination Sum II的方法分析复杂度了. 这里n'是新arr的大小

# Space: O(n)
# n: length of candidates
# worst case: candidates = [1,...] and target = n

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