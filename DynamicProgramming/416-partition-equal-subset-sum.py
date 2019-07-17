# -*- coding: utf-8 -*-

'''
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

# DP??
# Time: O(l * n)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum( nums )
        
        if total%2:
            return False
        
        target = total/2
        current = set( [0] )
        
        i = 0
        while i < len(nums) and current:
            nextlevel = set()
            for val in current:
                nextlevel.add( val + nums[i] )
            current = current.union( nextlevel )
            if target in current:
                return True
            i += 1
            
        return False