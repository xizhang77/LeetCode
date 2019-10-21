# -*- coding: utf-8 -*-

'''
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''
# Solution 1: Brute Force
# Time: O(n^2); Space: O(1)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        for i in range( len(nums) ):
            count = 0
            for j in range( i, len(nums) ):
                count += nums[j]
                if ((k==0 and count == 0) or (k != 0 and count%k == 0)) and (j-i) >= 1:
                    return True
        
        return False

# Soluiton 2: Hash Map
# Time and Space: O(n)

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        currsum = 0
        
        hashmap[ 0 ] = -1
        for i, val in enumerate( nums ):
            currsum += val
            
            if k != 0:
                currsum %= k
            
            if currsum in hashmap:
                if i - hashmap[ currsum ] > 1:
                    return True
            else:
                hashmap[ currsum ] = i
        
        return False