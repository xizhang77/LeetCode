# -*- coding: utf-8 -*-

'''
Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''

# Solution 1: Brute-Force
# Time: O(n^2) [LTE]
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = heights
        ans = 0
        for i in range(len(heights)):
            for j in range(i, -1, -1):
                temp = min(heights[j:i+1]) * (i - j + 1)
                ans = max(ans, temp)
        
        return ans


# Solution 2: Stack
'''
The stack maintain the indexes of buildings with ascending height. 
Before adding a new building pop the building who is taller than the new one. 
The building popped out represent the height of a rectangle with the new building 
as the right boundary and the current stack top as the left boundary. 
Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.
'''

# Time & Space: O(n)
# Worse case: insert all and pop out all
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [ -1 ]
        
        ans = 0
        for i in range( len(heights)):
            while heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                ans = max( ans, heights[idx]*(i - stack[-1] - 1) )
            stack.append(i)
        
        return ans