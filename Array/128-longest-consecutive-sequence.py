# -*- coding: utf-8 -*-

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        ans = 0
        for num in nums:
            if num in hashMap:
                continue
            
            start = end = num
            
            if num - 1 in hashMap:
                start = hashMap[ num-1 ][0]
            if num + 1 in hashMap:
                end = hashMap[ num+1 ][1]
            
            hashMap[ start ] = hashMap[ end ] = hashMap[ num ] = [ start, end ]
            
            ans = max(ans, end - start + 1)
        
        return ans