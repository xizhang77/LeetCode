class Solution(object):
	def dfs(self, nums, i, ans, subset):
		ans.append(subset)
		print ans
		for j in range(i, len(nums)):
			self.dfs(nums, j+1, ans, subset + [nums[j]])

	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		ans = []
		self.dfs(sorted(nums), 0, ans, [])
		print ans
		return ans


if __name__ == '__main__':
    S = Solution()
    S.subsets([1,2,3])