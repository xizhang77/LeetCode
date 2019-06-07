# -*- coding: utf-8 -*-

'''
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements 
to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

'''

# Solution 1: Insert Sort
# Refer: https://www.cnblogs.com/grandyang/p/5078490.html
# Time: O(nlogn); Space: O(n)
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [ 0 ] * n
        sort = []
        
        for k in range( n - 1, -1, -1 ):
            i, j = 0, len( sort )
            while i < j:
                mid = i + (j-i)/2
                if sort[ mid ] >= nums[k]:
                    j = mid
                else:
                    i = mid + 1
            res[ k ] = j
            sort.insert( j, nums[k])
        
        return res


# Solution 2: Binary Search Tree
# Later ... 