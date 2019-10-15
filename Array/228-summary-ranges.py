# -*- coding: utf-8 -*-

'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

# Time and Space: O(n)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """        
        if not nums:
            return []
        
        stack = [ [nums[0], nums[0]] ]
        
        for num in nums[1:]:
            if num - 1 == stack[-1][-1]:
                stack[-1][-1] = num
            else:
                stack.append( [num, num] )
        
        ans = []
        
        for interval in stack:
            start, end = interval
            if start == end:
                ans.append( str(start) )
            else:
                ans.append( str(start) + '->' + str(end) )
        
        return ans