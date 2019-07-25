# -*- coding: utf-8 -*-

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# Solution 1: Two pointer (Time: O(nlogn) due to the sorting function; Otherwise is O(n); Space: O(n))
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortNum = sorted( nums )
        
        i, j = 0, len(nums) - 1
        
        while i < j:
            temp = sortNum[i] + sortNum[j]
            if temp < target:
                i += 1
            elif temp > target:
                j -= 1
            else:
                if sortNum[i] != sortNum[j]:
                    return sorted([ nums.index(sortNum[i]), nums.index(sortNum[j])])
                else:
                    return sorted([idx for idx in range( len(nums)) if nums[idx] == sortNum[i]])


# Solution 2: Hash Table (Time: O(n); Space: O(n))
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        
        for i in range( len(nums) ):
            if nums[i] not in hashMap:
                hashMap[ nums[i] ] = [ i ]
            else:
                hashMap[ nums[i] ] += [ i ]
        
        for i in range( len(nums) ):
            if target - nums[i] in hashMap and target - nums[i] != nums[i]:
                return hashMap[ nums[i] ] + hashMap[ target - nums[i] ]
            elif target - nums[i] == nums[i] and len( hashMap[ nums[i] ] ) == 2:
                return hashMap[ nums[i] ]


# Solution 3: Binary Search (Time: O(nlogn))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort = sorted( nums, reverse = False )
        
        for k, num in enumerate( sort ):
            i, j = k+1, len(nums) - 1
            while i <= j:
                mid = i + (j-i)/2
                if sort[mid] > target - num:
                    j = mid - 1
                elif sort[mid] < target - num:
                    i = mid + 1
                else:
                    if num == sort[mid]:
                        return [idx for idx in range(len(nums)) if nums[idx] == num ]
                    else:
                        return sorted([nums.index(num), nums.index( sort[mid])])
