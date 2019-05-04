class Solution(object):
	def depthSum(self, nestedList):
		"""
		:type nestedList: List[NestedInteger]
		:rtype: int
		"""
		depth = 1
		ans = 0

		while nestedList:
			# Directly work on LeetCode instead