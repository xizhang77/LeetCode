class Solution(object):

	def dfs(self, nums, i, ans, subset):
		if len(subset) == 3 and sum(subset) == 0 and subset not in ans:
			ans.append(subset)
			return
		if (-sum(subset)) not in nums or len(subset) > 3:
			return

		for j in range(i, len(nums)):
			self.dfs(nums, j+1, ans, subset+ [nums[j]])


	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		ans = []
		self.dfs(sorted(nums), 0, ans, [])

		return ans



if __name__ == '__main__':
	s = Solution()
	print s.threeSum([-13,11,11,0,-5,-14,12,-11,-11,-14,-3,0,-3,12,-1,-9,-5,-13,9,-7,-2,9,-1,4,-6,-13,-7,10,10,9,7,13,5,4,-2,7,5,-13,11,10,-12,-14,-5,-8,13,2,-2,-14,4,-8,-6,-13,9,8,6,10,2,6,5,-10,0,-11,-12,12,8,-7,-4,-9,-13,-7,8,12,-14,10,-10,14,-3,3,-15,-14,3,-14,10,-11,1,1,14,-11,14,4,-6,-1,0,-11,-12,-14,-11,0,14,-9,0,7,-12,1,-6])
      