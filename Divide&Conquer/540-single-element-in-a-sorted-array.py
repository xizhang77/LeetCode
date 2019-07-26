# -*- coding: utf-8 -*-

'''
Given a sorted array consisting of only integers where every element appears 
exactly twice except for one element which appears exactly once. 
Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.

'''

# Time: O(logn); Space: O(1)
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i, j = 0, len(nums) 
        
        while j - i > 1:
            idx = (j-i)/2
            if nums[i+idx] != nums[i+idx+1]:
                if idx%2 == 0:
                    j = i + idx + 1
                else:
                    i = i + idx + 1
            else:
                if idx%2 == 0:
                    i = i + idx + 2
                else:
                    j = i + idx
        
        return nums[i]

# Time and Space: O(logn)
class Solution2(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def dfs(start, end):
            if end - start == 1:
                return nums[ start ]
            
            idx = (end-start)/2
            
            if nums[start+idx] != nums[start+idx+1]:
                if idx%2 == 0:
                    return dfs( start, start+idx+1 )
                else:
                    return dfs( start+idx+1, end )
            else:
                if idx%2 == 0:
                    return dfs( start+idx+2, end )
                else:
                    return dfs( start, start + idx )
        
        return dfs( 0, len(nums) )

# Time: O(logn) but not O(1) Space
class Solution3(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        n = len(nums)
                
        if n == 1:
            return nums[0]
        
        idx = n/2
        
        if nums[idx] != nums[idx+1]:
            if idx%2 == 0:
                return self.singleNonDuplicate( nums[:idx+1] )
            else:
                return self.singleNonDuplicate( nums[idx+1:] )
        else:
            if idx%2 == 0:
                return self.singleNonDuplicate( nums[idx+2:] )
            else:
                return self.singleNonDuplicate( nums[:idx] )