# -*- coding: utf-8 -*-

'''
Given a set of non-overlapping intervals, 
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their 
start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# Solution 1
# Time: O(n); Space: O(n) (due to range) 2 paths
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [ newInterval ]
        
        n = len(intervals)
        for i in range( n ):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert( i, newInterval )
                break
            if i == n - 1:
                intervals.insert( i+1, newInterval )
        n += 1
        i = 0
        while i < n:
            if i + 1 < n and intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max( intervals[i][1], intervals[i+1][1] )
                intervals.pop( i+1 )
                n -= 1
            else:
                i += 1

# Solution 2
# Time: O(n); 1 path
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals or newInterval[1] < intervals[0][0]:
            intervals.insert( 0, newInterval )
            return intervals
        
        if  newInterval[0] > intervals[-1][1]:
            intervals.append( newInterval )
            return intervals
        
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                i += 1
            else:
                intervals.insert( i, newInterval )
                while i + 1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                    temp = intervals.pop( i+1 )
                    intervals[i] = [ min(intervals[i][0], temp[0]), max(intervals[i][1], temp[1]) ]
                break
        
        return intervals 
        return intervals