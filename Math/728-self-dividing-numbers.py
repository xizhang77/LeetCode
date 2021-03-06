# -*- coding: utf-8 -*-


'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, 
including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''

# Time: O( (right-left)*len(right) )
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        
        for i in range(left, right + 1):
            num = i
            flag = 1
            while i:
                div = i%10
                if div == 0 or num%div != 0:
                    flag = 0
                    break
                i = i/10
            if flag:
                ans.append( num )
        
        return ans