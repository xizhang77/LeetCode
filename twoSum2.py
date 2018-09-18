'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		sortnums = sorted(nums)

		i = 0
		j = len(nums) - 1

		while i < j:
			if sortnums[i] + sortnums[j] < target:
				i += 1
			elif sortnums[i] + sortnums[j] > target:
				j -= 1
			else:
				if sortnums[i] == sortnums[j]:
					return [idx for idx in xrange(len(nums))f if nums[idx] == sortnums[i]]
				else:
					return [nums.index(sortnums[i]), nums.index(sortnums[j])]

obj = Solution()
# print obj.twoSum([2, 7, 11, 15], 9)
print obj.twoSum([2,5,5,11], 10)