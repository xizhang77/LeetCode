import collections

class Solution(object):
	def leastInterval(self, tasks, n):
		"""
		:type tasks: List[str]
		:type n: int
		:rtype: int
		"""
		taskcount = collections.Counter(tasks).values()
		M = max(taskcount)
		numMax = taskcount.count(M)
		print numMax
		return max(len(tasks), (M-1)*(n+1) + numMax)



if __name__ == '__main__':
	s = Solution()
	print s.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2)
