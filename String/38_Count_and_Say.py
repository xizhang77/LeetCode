# -*- coding: utf-8 -*-

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

# Time: O(???); Space: O(n) (n is the length of the output)
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        
        if n <= 1:
            return ans
        
        for i in range( n - 1 ):
            temp = list(ans)
            ans = ''
            j = 0
            while j < len(temp):
                target = temp[j]
                count = 1
                while j + 1 < len(temp) and temp[j] == temp[ j+1 ]:
                    j += 1
                    count += 1
                ans += str(count) + target
                j += 1
            
        return ans