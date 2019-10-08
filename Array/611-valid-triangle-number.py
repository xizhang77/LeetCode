# -*- coding: utf-8 -*-

'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''
# Solution 1: Two Pointer
# Time: O(n^2); Space: O(1)
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        
        while nums and nums[-1] == 0:
            nums.pop()
            
        ans = 0
        for i in range( len(nums)-2 ):
            target = nums[i]
            
            p, q = i+1, len(nums) - 1
            
            while p < q:
                if nums[p] + nums[q] > target:
                    ans += q - p
                    p += 1
                else:
                    q -= 1
        
        return ans

# Time: O(n^2logn); Space: O(1)
class Solution(object):
    def binarySearch(self, nums, start, target):
        if nums[-1] < target:
            return len(nums) 
        if nums[start] >= target:
            return start
        
        p, q = start, len(nums) - 1
        while p < q:
            mid = p + (q-p)/2
            if nums[mid] < target:
                p = mid + 1
            else:
                q = mid
        return p
    
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        while nums and nums[0] == 0:
            nums.pop( 0 )
            
        ans = 0
        
        for i in range( len(nums) - 2 ):
            for j in range( i+1, len(nums) - 1 ):
                target = nums[i] + nums[j]
                ans += self.binarySearch( nums, j + 1, target ) - j - 1
                # print nums[i], nums[j] ,ans 
        
        return ans