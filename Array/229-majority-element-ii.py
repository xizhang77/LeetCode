# -*- coding: utf-8 -*-

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

'''

# Time: O(n); Space: O(1)
# 和LeetCode 169 的思路一样，因为 > n/3 的数字在整个数组中只可能有两个，故设置2个candidates。
# 最后再遍历数组，计算candidates的个数，看是否符合 < n/3
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [ None, None ]
        
        count = [ 0, 0 ]
        
        for num in nums:           
            if num == ans[0]:
                count[0] += 1
            elif num == ans[1]:
                count[1] += 1
            elif count[0] == 0:
                ans[0], count[0] = num, 1            
            elif count[1] == 0:
                ans[1], count[1] = num, 1 
            else:
                count[0] -= 1
                count[1] -= 1
        
        count = [ 0, 0 ]
        
        for num in nums:
            if num == ans[0]:
                count[0] += 1
            elif num == ans[1]:
                count[1] += 1
        
        return [ ans[i] for i in range(2) if count[i] > len(nums)/3 ]