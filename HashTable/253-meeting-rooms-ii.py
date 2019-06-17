# -*- coding: utf-8 -*-

'''
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition 
to get new method signature.
'''

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted( intervals, key=lambda x:x[0])
        
        hashmap = {}
        
        for meet in intervals:
            start, end = meet
            flag = 1
            for key in hashmap:
                if hashmap[ key ] <= start:
                    flag = 0
                    hashmap[ key ] = end
                    break
            if flag:
                hashmap[ len(hashmap) + 1 ] = end
                
        return len(hashmap)