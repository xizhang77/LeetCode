# -*- coding: utf-8 -*-

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

# Time: O(n^2)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 1
        for i in range( len(nums) - 1, 0, -1 ):
            if not flag:
                break
            if nums[i-1] < nums[i]:
                for j in range( len(nums) - 1, i-1, -1 ):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        nums[i:] = sorted(nums[i:], reverse = False)
                        flag = 0
                        break
                
        if flag:
            nums.sort( reverse = False )