# -*- coding: utf-8 -*-

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

# Time: O(n^2)?
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0
        
        n = len(nums)
        
        dp = [ float('inf') ] * n    
        dp[0] = 0
        
        for i in range( n ):
            if i + nums[i] >= n - 1:
                return dp[i] + 1
            for j in range( i+1, i + nums[i] + 1 ):
                dp[j] = min( dp[j], dp[i] + 1 )

                if j + nums[j] >= n - 1:
                    return dp[j] + 1
                
        
                
