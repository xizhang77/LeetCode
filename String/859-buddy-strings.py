# -*- coding: utf-8 -*-

'''
Given two strings A and B of lowercase letters, return true if and only if 
we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

'''

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if A == B:
            seen = set()
            for char in A:
                if char not in seen:
                    seen.add( char )
                else:
                    return True
            return False
        
        i, j = 0, len(A) - 1
        
        while i < j and A[i] == B[i]:
            i += 1
        while i < j and A[j] == B[j]:
            j -= 1
            
        temp = A[:i] + A[j] + A[i+1:j] + A[i] + A[j+1:]
        
        return temp == B