# -*- coding: utf-8 -*-

'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

# Time and Space: O(N!)
# in the first level of the tree, you have N options and for each of the option, you have N-1 option, 
# and for each of these N-1 options, you have another N-2 options, 
# so putting them together you would end up N*(N-1)*(N-2).... = N!

class Solution(object):
    def dfs(self, nums, ans, path):
        if not nums:
            ans.append( path )
            return
        
        for i in range( len(nums) ):
            self.dfs( nums[:i]+nums[i+1:], ans, path + [nums[i]])
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( nums, ans, [] )
        
        return ans