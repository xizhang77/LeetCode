# -*- coding: utf-8 -*-

'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

1. What if the given array is already sorted? How would you optimize your algorithm?
2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
3. What if elements of nums2 are stored on disk, and the memory is limited 
such that you cannot load all elements into the memory at once?
'''

# Solution 1: Counter / Hash Map
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter( nums1 )
        count2 = Counter( nums2 )
        
        if len(count1) > len(count2):
            count1, count2 = count2, count1
        
        ans = []
        
        for val in count1:
            if val in count2:
                ans += [ val ] * min(count1[val], count2[val])
        
        return ans

# Solution 2: Binary Search
# Later...