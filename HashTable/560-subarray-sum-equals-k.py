# -*- coding: utf-8 -*-

'''
Given an array of integers and an integer k, you need to find the total number of 
continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and 
the range of the integer k is [-1e7, 1e7].
'''

# Solution 1
# Time and Space: O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = [ 0 ]
        hashMap = {}
        for i in range( len(nums) ):
            temp = nums[i] + left[-1]
            left.append( temp )
            
            if temp not in hashMap:
                hashMap[ temp ] = [ i ]
            else:
                hashMap[ temp ] += [ i ]
        
        ans = 0
        for i in range( len(nums) + 1 ):
            if left[i] + k in hashMap:
                for val in hashMap[ left[i] + k ]:
                    ans += 1 if val >= i else 0
        
        return ans

# Solution 2: more efficient than solution 1
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashMap = {0: 1}
        
        ans = cumSum = 0
        
        for i in range( len(nums) ):
            cumSum += nums[i]
            
            if cumSum - k in hashMap:
                ans += hashMap[ cumSum - k ]
            
            if cumSum not in hashMap:
                hashMap[ cumSum ] = 1
            else:
                hashMap[ cumSum ] += 1
                
            
        return ans