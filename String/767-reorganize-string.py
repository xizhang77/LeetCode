# -*- coding: utf-8 -*-

'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''


# Time: O(nlogn) (for the sort(count) )
# Space: O(n)
from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        
        n = len(S)
        count = Counter(S)
        
        for val in count.values():
            if (n%2 and val > n/2 + 1) or (not n%2 and val > n/2):
                return ""
            
        ans = [""]*n
        
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        i = j = 0
        temp = 0
        step = n
        while step > 0:
            # print ans, step
            ans[ i ] = count[j][0]
            temp += 1
            step -= 1
            i += 2
            
            if count[j][1] == temp:
                temp = 0
                j += 1
            if i >= n:
                i = 1
        return "".join(ans)
