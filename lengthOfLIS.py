# -*- coding: utf-8 -*-
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution(object):
	"""
	This solution is O(n^2) time complexity using only DP. Beat 39%. Can be improved.
	"""
	def lengthOfLIS_slow(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0

		n = len(nums)
		dp = [1] * n
		for i in range(n):
			for j in range(i):
				if nums[j] < nums[i]:
					dp[i] = max( dp[i], dp[j]+1 )
		print dp
		return max(dp)
	
	"""
	Another solution witn O(nlogn) time complexity using DP and binary search. Beat 100%
	"""	
	# Find the first number that is bigger than target. Return the index
	def binarySearch(self, nums, target):
		if nums[0] > target:
			return 0

		start, end = 0, len(nums)-1
		while (end + start)/2 not in [start, end]:
			if nums[ (end + start)/2 ] < target:
				start = (end + start)/2
			else:
				end = (end + start)/2

		return end

	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		
		path = [nums[0]]
		for num in nums[1:]:
			print path
			if num > path[-1]:
				path.append(num)
			elif num < path[-1] and num not in path:
				idx = self.binarySearch(path, num)
				path[idx] = num

		return len(path)


obj = Solution()
# print obj.lengthOfLIS([10,9,2,5,3,7,101,18])

print obj.lengthOfLIS([4,10,4,3,8,9])
