# -*- coding: utf-8 -*-
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Could you solve it without converting the integer to a string?
'''

# Solution 1 (Time: O(n); Space: O(n))
class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return str(x) == str(x)[::-1]

# Solution 2: Two Pointer (Time: O(n); Space: O(n))
class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        
        p, q = 0, len(x) - 1
        
        while p < q:
            if x[p] != x[q]:
                return False
            p += 1
            q -= 1
        
        return True



# Solution 3: Without converting to string
class Solution3(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev, num = 0, x
        
        while num > 0 :
            rev = rev*10 + num%10
            num = num/10
            
        return rev == x