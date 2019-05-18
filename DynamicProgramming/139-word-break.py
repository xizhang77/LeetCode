# -*- coding: utf-8 -*-

'''
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.
'''

# Time: O(n^2); Space: O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        
        dp = [ False for _ in range( n + 1 ) ]
        
        dp[0] = True
        
        for i in range( n ):
            for j in range(i, -1 , -1):
                if s[j:i+1] in wordDict and dp[j]:
                    dp[i+1] = True
                    break
        return dp[-1]