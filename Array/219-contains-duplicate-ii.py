# -*- coding: utf-8 -*-

'''
Given an array of integers and an integer k, find out whether there are 
two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

# Solution 1: Hash Table
# Time & Space: O(n)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        
        for i in range( len(nums) ):
            if nums[i] in hashMap:
                if i - hashMap[ nums[i] ] <= k:
                    return True
            hashMap[ nums[i] ] = i
        return False

# Solution 2: Set
# Time: O(n); Space: O(k)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        check = set()
        
        for i in range( len(nums) ):
            if nums[i] in check:
                return True
            check.add( nums[i] )
            if len( check ) > k:
                check.remove( nums[i-k] )
            
        return False