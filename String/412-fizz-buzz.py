# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/fizz-buzz/
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        i = 1
        while i <= n:
            if i%3 == 0 and i%5 != 0:
                ans.append( 'Fizz' )
            elif i%3 != 0 and i%5==0:
                ans.append( 'Buzz' )
            elif i%3 == 0 and i%5 == 0:
                ans.append( 'FizzBuzz' )
            else:
                ans.append( str(i) )
            i += 1
            
        return ans