'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
'''



'''
This is not the correct answer. The question is asked for "subarray", not "subset"

'''
class Solution(object):
	def dfs(self, nums, target, start, subset, ans):
		print subset
		if sum(subset) == target:
			self.ans = max(self.ans, len(subset))
			print self.ans
			return 
		elif sum(subset) > target:
			return 
		else:
			for i in range(start, len(nums)):
				self.dfs(nums, target, i+1, subset + [nums[i]], self.ans)

	def maxSubArrayLen(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""

		self.ans = 0
		self.dfs(sorted(nums), k, 0, [], self.ans)
		return self.ans

obj = Solution()
print obj.maxSubArrayLen([-2, -1, 2, 1], 1)
