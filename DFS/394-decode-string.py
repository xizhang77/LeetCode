# -*- coding: utf-8 -*-

'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits 
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

'''

# Solution 1: DFS
# Time and Space: O(n)
class Solution(object):
    def dfs(self, s ):
        ans = ""
        char = num = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == '[':
                val, idx = self.dfs( s[i+1:] )
                i += idx
                ans += char + int( num ) * val
                num = char = ""
            elif s[i] == ']':
                break
            else:
                char += s[i]
            i += 1
        
        return ans + char, i + 1
    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return self.dfs( s )[0]



# Solution 1: Stack [Refer to a sample 8ms submission]
# Time and Space: O(n)

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [ ["", 1] ]
        
        num = ""
        
        for i in range( len(s) ):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == '[':
                stack.append( ["", int(num)])
                num = ""
            elif s[i] == ']':
                val, digit = stack.pop()
                stack[-1][0] += val*digit
            else:
                stack[-1][0] += s[i]
                    
        return stack[0][0]