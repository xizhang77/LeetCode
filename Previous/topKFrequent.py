from collections import Counter

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""

		return [ num for num, num_count in Counter(nums).most_common(k)]


obj = Solution()
print obj.topKFrequent([1,1,1,2,2,3,3,3], 3)
