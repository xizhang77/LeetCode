'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

from collections import Counter

class Solution(object):
	def subarraySum(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		table = Counter({0:1})

		summation = 0
		count = 0
		for num in nums:
			summation += num
			count += table[summation - k]
			table[summation] += 1
			print table, summation

		return count

obj = Solution()
print obj.subarraySum([1,2,1,7,-3,4], 4)