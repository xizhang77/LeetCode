'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution(object):
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums = sorted(nums)
		n = len(nums)
		ans = []

		i = 0
		while i < n:
			print i 
			if nums[i] >= target and nums[i] > 0:
				return ans
			j = i + 1
			while j < n:
				summation = nums[i] + nums[j]
				if summation >= target and summation > 0:
					break
				k = j + 1
				l = n - 1
				while k < l:
					if summation + nums[k] + nums[l] == target:
						ans.append( [nums[i], nums[j], nums[k], nums[l]] )
						while nums[k] == nums[k+1] and k < l:
							k += 1
						k += 1
						while nums[l] == nums[l-1] and k < l:
							l -= 1
						l -= 1
					elif summation + nums[k] + nums[l] < target:
						while nums[k] == nums[k+1] and k < l:
							k += 1
						k += 1
					else:
						while nums[l] == nums[l-1] and k < l:
							l -= 1
						l -= 1
				while j < n - 1 and nums[j] == nums[j+1]:
					j += 1
				j += 1
			while i < n - 1 and nums[i] == nums[i+1]:
				i += 1
			i += 1

		return ans

obj = Solution()
# print obj.fourSum([1, 0, -1, 0, -2, 2], 0)

print obj.fourSum([-3,-2,-1,0,0,1,2,3], 0)