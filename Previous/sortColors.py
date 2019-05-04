# -*- coding: utf-8 -*-
'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''

from collections import Counter
class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		count = Counter(nums)
		if len(count) == 1:
			return
		else:
			value = count.values()
			key = count.keys()
			for i in range(len(nums)):
				if i < value[0]:
					nums[i] = key[0]
				elif i >= value[0] and i < value[0] + value[1]:
					nums[i] = key[1]
				else:
					nums[i] = key[2]

obj = Solution()
print obj.sortColors([2,0,2,1,1,0])