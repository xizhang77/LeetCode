# -*- coding: utf-8 -*-

'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
'''

# Solution 1 [Backtracking]: Beat 5% ...
class Solution(object):
    def dfs(self, n, last, ans ):
        if len(ans) == 2**n:
            return
        temp = int("".join(last), 2)
        if temp in ans:
            return
        ans.append( temp )
        
        for i in range( 1, n + 1 ):
            if last[i] == '0':
                self.dfs( n, last[:i]+['1']+last[i+1:], ans)
            else:
                self.dfs( n, last[:i]+['0']+last[i+1:], ans)
        
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = []
        self.dfs( n, ['0']*(n+1), ans )
        
        return ans

# Solution 2 [Bit & Math]