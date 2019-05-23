# -*- coding: utf-8 -*-

'''
Given a string S and a string T, count the number of 
distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from 
the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''

# Solution 1 [BFS, LTE]
class Solution(object):
    def dfs(self, string, hashMap, index):
        if not string:
            self.count += 1
            return
        char = string[0]
        idx = hashMap[ char ]
        for i in idx:
            if i > index:
                self.dfs( string[1:], hashMap, i )
                
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if set(t) - set(s):
            return 0
        if s == t:
            return 1
        
        self.count = 0
        
        hashMap = {}
        
        for char in t:
            if char not in hashMap:
                hashMap[ char ] = [ idx for idx in range(len(s)) if s[idx] == char ]
        
        self.dfs( t, hashMap, -1 )
        
        return self.count

# Solution 2: DP
# Time & Space: O(m*n)
'''
Refer: https://blog.csdn.net/XX_123_1_RJ/article/details/80789223

标准动态规划题目，dp[i][j]表示字符串S[0:j] 中有多少个 T[0:i]
当i=2，j=6时，表示字符串 'babgbag' 中有多少个 'bag'
此时，要想知道现在有多少个'bag', 那么只需知道 j=5 时有多少个 'ba' 和已经有了多少个'bag', 
接着再判断 S[j] ==T[i] 是否成立，如果成立，dp[i][j] = 'ba'的个数 + 已有'bag'的个数，
dp[i][j] = 已有'bag'的个数。
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s == t:
            return 1
        if set(t) - set(s):
            return 0
        
        m, n = len(s), len(t)
        
        dp = [ [0]*m for _ in range(n) ]
        
        for j in range( n ):
            dp[j][ 0 ] = 1 if t[:j+1] == s[0] else 0
        
        for i in range( 1, m ):
            dp[0][i] = dp[0][i-1] + (s[i] == t[0])
        
        
        for i in range( 1, n ):
            for j in range( 1, m ):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1] * (s[j] == t[i])
        
        return dp[-1][-1]


# Solution 3: DP
# Time: O(m*n); Space: O(m)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s == t:
            return 1
        if set(t) - set(s):
            return 0
        
        m, n = len(s), len(t)
        
        dp = [0] * m
        dp[0] = 1 if s[0] == t[0] else 0
        
        for j in range( 1, m ):
            dp[j] = dp[j-1] + (s[j] == t[0])
        
        
        for i in range( 1, n ):
            temp = []
            for j in range( m ):
                if j == 0:
                    temp += [ 1 ] if s[0] == t[:i+1] else [0]
                else:
                    temp.append( temp[-1] + dp[j-1] * (s[j] == t[i]) )
            dp = temp

        return dp[-1]