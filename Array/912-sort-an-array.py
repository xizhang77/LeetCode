# -*- coding: utf-8 -*-

'''
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]

Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Note:

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

'''

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        
        for num in nums:
            if num not in hashmap:
                hashmap[ num ] = 1
            else:
                hashmap[ num ] += 1
        
        ans = []
        
        for key in sorted(hashmap.keys()):
            ans += [ key ]*hashmap[ key ]
        
        return ans