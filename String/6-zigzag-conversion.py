# -*- coding: utf-8 -*-

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

'''

# Time: O(n); Space: O(n/numRows)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        
        n = len(s)
        ans = ""
        gap = numRows*2 - 2
        
        for i in range( numRows ):
            temp = ""
            if i == 0 or i == numRows - 1:
                p = i
                while p < n:
                    temp += s[p]
                    p += gap
            else:
                p, q = i, gap - i
                while p < n:
                    temp += s[p]
                    p += gap
                    if q < n:
                        temp += s[q]
                        q += gap
                
            ans += temp
        
        return ans