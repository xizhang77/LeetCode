'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""

		intervals.sort( key=lambda x: x[0])
		print intervals

		i = 0
		while i < len(intervals) - 1:
			if intervals[i+1][0] <= intervals[i][1]:
				intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
				intervals.pop(i+1)
			else:
				i += 1

		print intervals

obj = Solution()
# obj.merge([[1,3],[2,6],[8,10],[15,18]])

obj.merge([[1,4],[2,3]])