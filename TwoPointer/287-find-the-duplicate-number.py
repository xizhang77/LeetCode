# -*- coding: utf-8 -*-

'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once
'''

# Soluiton 1: Sorting
# Time: O(nlgn) due to the sorting function
# Space: O(n) [Doesn't satisfy the 2nd requirment]
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)
        
        for i in range( len(sort) - 1 ):
            if sort[i] == sort[ i+1 ]:
                return sort[i]

# Solution 2: Hash Table / Set
# Time & Space: O(n) [Doesn't satisfy the 2nd requirment]

# Soluiton 3 [Linked List??]
# Refer to LeetCode 142: https://leetcode.com/problems/linked-list-cycle-ii/
'''
那么如果序列是重复的，[1,3,3,2]，那么下标对应数字时会有重复，路径就会出现环！
0->1->3->2->3->2…，会出现3 2 这个环，那么环开始的地方就是重复的数字。
这时就可以利用LeetCode.142 中的方法找到环起始的位置。
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = finder = 0
        
        while True:
            slow = nums[ slow ]
            fast = nums[ nums[ fast ] ]
            
            if slow == fast:
                while slow != finder:
                    finder = nums[ finder ]
                    slow = nums[ slow ]
                return finder
