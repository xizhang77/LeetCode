# -*- coding: utf-8 -*-

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution(object):

	def findKthLargest2(self, nums, k):
		nums.sort(reverse=Ture)

		return nums[k-1]
		
	def findKthLargest(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		nums = sorted(nums)

		return nums[len(nums) - k]


obj = Solution()
print obj.findKthLargest([3,2,3,1,2,4,5,5,6], 4)