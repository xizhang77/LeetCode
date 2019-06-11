# -*- coding: utf-8 -*-

'''
Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums1, nums2 = list(num1), list(num2)
        
        if len(nums1) == 0:
            return num2
        if len(nums2) == 0:
            return num1
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        p, q = len(nums1) - 1, len(nums2) - 1
        res = 0
        
        while q >= 0:
            temp = res + int(nums1[p]) + int(nums2[q])
            nums1[p] = str( temp%10 )
            res = temp/10
            p -= 1
            q -= 1
        
        while p >= 0:
            temp = res + int(nums1[p])
            nums1[p] = str( temp%10 )
            res = temp/10
            p -= 1

        if res:
            nums1 = [ str(res) ] + nums1
            
        return "".join(nums1)