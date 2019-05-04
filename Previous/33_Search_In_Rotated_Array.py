# -*- coding: utf-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution(object):
	def binarySearch2(self, nums, target):
		if nums[0] > target or nums[-1] < target:
			return -1
		start, end = 0, len(nums) - 1
		while (end - start) > 1:
			if nums[ (start + end)/2 ] < target:
				start = (start + end)/2
			else:
				end = (start + end)/2

		if target not in [nums[start], nums[end]]:
			return -1
		else:
			return start if target == nums[start] else end

	def binarySearch(self, nums, target):
		if nums[0] > target or nums[-1] < target or not nums:
			return -1

		start, end = 0, len(nums) - 1
		while 1:
			if nums[start] == target or nums[end] == target:
				return start if nums[start] == target else end

			if nums[ (start + end)/2 ] > target:
				end = (start + end)/2
			else:
				start = (start + end)/2
			
			if end - start == 1 and nums[start] != target and nums[end] != target:
				break

		return -1


	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return -1
		if len(nums) == 1:
			return 0 if nums[0] == target else -1

		# check rotation
		start, end = 0, len(nums) - 1
		if nums[start] > nums[end]:
			while (start + end)/2 not in [start, end]:
				if nums[(start + end)/2] > nums[start]:
					start = (start + end)/2
				else:
					end = (start + end)/2

			if nums[0] > target:
				ans = self.binarySearch( nums[end:], target) 
				if ans != -1:
					return end + ans
			else:
				ans = self.binarySearch( nums[:start+1], target)
		else:
			ans = self.binarySearch( nums, target)

		return ans




obj = Solution()
print obj.search( [4,5,6,7,9,0,1,2], 3)
# print obj.search( [1,3], 3)

# print obj.search( [3,1], 1)