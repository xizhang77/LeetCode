# -*- coding: utf-8 -*-

'''
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). 
If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).

'''

class Solution(object):
	def maxSumOfThreeSubarrays(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		n = len(nums)
		MIN = - float('inf')

		sumk = [0] * (n - k + 1)

		for i in range(n - k + 1):
			if i == 0:
				sumk[i] = sum(nums[:k])
			else:
				sumk[i] = sum[i-1] + nums[i-k+1] - nums[i-1]
		print sumk

		left = [MIN] * n
		temp = sumk[0]
		left[k-1] = 0
		for i in range(k, n):
			if sumk[i-k+1] > temp:
				temp = sumk[i-k+1]
				left[i] = i - k + 1
			else:
				left[i] = left[i-1]
		print left

		right = [MIN] * n
		temp = sumk[-1]
		right[-k] = n - k
		for i in range(n-k-1, -1, -1):
			if sumk[i] > temp:
				temp = sumk[i]
				right[i] = i
			else:
				right[i] = right[i+1]
		print right
		
		ans = []
		total = MIN
		for i in range(k-1, n-2*k):
			l = left[i]
			r = right[i + k + 1]
			print i, l, r, sumk[i+1]
			temp = sumk[l] + sumk[r] + sumk[i+1]
			if temp > total:
				total = temp
				ans = [l, i+1, r]

		return ans

obj = Solution()
# print obj.maxSumOfThreeSubarrays( [1,2,1,2,6,7,5,1], 2 )
print obj.maxSumOfThreeSubarrays( [7,13,20,19,19,2,10,1,1,19], 3)
