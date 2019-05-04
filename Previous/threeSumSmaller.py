# -*- coding: utf-8 -*-

'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k 
with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
'''

class Solution(object):
	def threeSumSmaller(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums = sorted(nums)

		ans = 0
		summation = 0

		for i in range(len(nums)):
			if nums[i] >= target and nums[i] > 0:
				break
				
			j = i + 1
			k = len(nums) - 1
			while j < k:
				summation = nums[i] + nums[j] + nums[k]
				if summation >= target:
					k -= 1
				else:
					ans += (k-j)
					j += 1

		return ans

obj = Solution()
# print obj.threeSumSmaller([-2,0,1,3, 7, -4], 2)
# print obj.threeSumSmaller([-1, 1, -1, -1], -1)
print obj.threeSumSmaller([0,-4,-1,1,-1,2], -5)
