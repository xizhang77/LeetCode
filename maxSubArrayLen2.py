'''
It's LTE. Try another method...
'''

class Solution(object):
	def maxSubArrayLen(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""

		ans = 0
		for i in range(len(nums)):
			summation = 0
			for j in range(i, len(nums)):
				summation += nums[j]
				if summation == k:
					ans = max(ans, j-i+1)

		return ans

obj = Solution()
print obj.maxSubArrayLen([-2, -1, 2, 1], 1)
print obj.maxSubArrayLen([1, -1, 5, -2, 3], 3)
print obj.maxSubArrayLen([-1], -1)
