# -*- coding: utf-8 -*-

'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''

# Solution 1
class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        total = len(nums)
        i = 0
        
        while i < total:
            target = nums[i]
            while i + 1 < total and nums[i+1] == target:
                nums.pop( i+1 )
                total -= 1
                
            i += 1
        
        return total


# Solution 2: Use two pointers (Cannot pass the OJ because the var: nums doesn't change; But the solution itself works)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        
        i = 0
        
        while i < total:
            target = nums[i]
            j = i + 1
            while j < total and nums[j] == target:
                j += 1
                total -= 1
            nums = nums[:i+1] + nums[j:]

            i = i + 1
            
        return total

# Solution 3: [AC version with two pointers]
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        
        i = 0
        j = 0
        while j < total:
            while j + 1 < total and nums[j + 1] == nums[i]:
                j += 1
            
            if j + 1 < total:
                nums[ i + 1 ] = nums[ j + 1 ]
                i += 1
            j += 1
            
        return i + 1

# Solution 4: [AC version with two pointers, faster than Solution 3]
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len( nums )
        
        i = 0
        
        for j in range( total - 1 ):
            if nums[j] != nums[ j + 1 ]:
                i += 1
                nums[i] = nums[j+1]
        
        return i + 1
