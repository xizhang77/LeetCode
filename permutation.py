'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
	def dfs(self, nums, subset, ans):
		if not nums:
			# Attention: ans.append(subset) doesn't work but ans.append( list(subset) ) works.
			# One possible result is that when directly append subset to ans, some kind of obj/pointer is appended instead.
			ans.append( list(subset) )
			return 

		for i in range(len(nums)):
			subset.append( nums.pop(i) )
			self.dfs( nums, subset, ans )
			nums.insert( i, subset.pop() )

	def permute(self, nums):

		ans = []
		self.dfs( sorted(nums), [], ans)

		return ans


obj = Solution()

print obj.permute([1,2,3])