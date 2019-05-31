# -*- coding: utf-8 -*-

'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

# 不太清楚这道题到底想考什么…所以就挑了一个最直接的解法…
class Solution(object):
    def addList(self, num1, num2):
        m , n = len(num1), len(num2)
        i = j = res = 0
        ans = []
        while i < m and j < n:
            temp = num1[i] + num2[j] + res
            res = temp/10
            ans.append( temp%10 )
            i, j = i + 1, j + 1
        
        while i < m:
            temp = num1[i] + res
            res = temp/10
            ans.append( temp%10 )
            i += 1
            
        while j < n:
            temp = num2[j] + res
            res = temp/10
            ans.append( temp%10 )
            j += 1
        
        if res:
            ans.append( res )
        
        return ans 
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        
        num1, num2 = list( num1 ), list( num2 )
        
        ans = []
        for a in num2:
            res = 0
            temp = []
            for b in num1[::-1]:
                c = int(a) * int(b) + res
                res = c/10
                temp += [ c%10 ]
            if res:
                temp += [ res ]
            
            ans = [ 0 ] + ans
            ans = self.addList( ans, temp )
            
        return "".join( [str(num) for num in ans[::-1] ])
