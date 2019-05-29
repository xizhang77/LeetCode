# -*- coding: utf-8 -*-

'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower, upper = 1, n
        
        if guess( lower ) == 0:
            return lower
        if guess( upper ) == 0:
            return upper
        
        while True:
            ans = (lower + upper)/2
            if guess( ans ) == -1:
                upper = min( upper, ans )
            elif guess( ans ) == 1:
                lower = max( lower, ans )
            else:
                return ans
            
       