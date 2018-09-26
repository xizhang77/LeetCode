# -*- coding: utf-8 -*-
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		MIN = - float('inf')

		dp = [MIN] * len(nums)
		dp[0] = nums[0]

		for i in range(1, len(nums)):
			dp[i] = max( nums[i], dp[i-1] + nums[i] )

		print dp

		return max(dp)

obj = Solution()
print obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])