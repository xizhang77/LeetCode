# -*- coding: utf-8 -*-

'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls 
to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


# Time : O(logn)
# Attention: Using mid = i + (j-i)/2 instead of (i+j)/2 
# since the latter one can exceed the integer limit whereas former one
# doesn't exceed the integer bounds.

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 0, n
        
        if isBadVersion(0):
            return 0
        
        while i <= j:
            mid = i + (j-i)/2
            if isBadVersion( mid ):
                j = mid - 1
            else:
                i = mid + 1
        
        return i