# -*- coding: utf-8 -*-

'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

# Solution 1: Time O(n); Space: O(1)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 1
        i = len(digits) - 1
        
        while res and i >= 0 :
            temp = digits[i] + res
            digits[i] = temp%10
            res = temp/10
            i -= 1
            
        if res:
            digits = [res] + digits
        
        return digits
