# -*- coding: utf-8 -*-

'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

HINT: https://en.wikipedia.org/wiki/Digital_root
'''

 
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = str(num)
        
        while len(ans) > 1:
            temp = 0
            for c in ans:
                temp += int(c)
            ans = str(temp)
        
        return int(ans)

# Follow up
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        return 0 if not num else 1 + (num-1) % 9