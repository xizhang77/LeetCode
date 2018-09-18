'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def minMeetingRooms(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: int
		"""
		if not intervals:
			return 0

		intervals.sort( key=lambda x: x[0])
		stack = [0]

		for interval in intervals:
			idx = [ x for x in range(len(stack)) if interval[0] >= stack[x] ]
			if idx:
				stack[idx[0]] = interval[1]
			else:
				stack.append(interval[1])
		return len(stack)

obj = Solution()
print obj.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
print obj.minMeetingRooms([[7,10],[2,4]])
print obj.minMeetingRooms([[13,15],[1,13]])
print obj.minMeetingRooms([[1,8],[6,20],[9,16],[13,17]])