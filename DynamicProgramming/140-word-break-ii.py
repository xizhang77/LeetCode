# -*- coding: utf-8 -*-

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

# Time: O(n^2); 
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # To avoid memory LE, check if it contains a valid break first
        n = len(s)
                
        dp = [ False for _ in range( n + 1 ) ]
        
        dp[0] = True
        
        for i in range( n ):
            for j in range(i, -1 , -1):
                if s[j:i+1] in wordDict and dp[j]:
                    dp[i+1] = True
                    break
        
        if dp[-1] == False:
            return []
        

        
        hashMap = {0: ['']}
        
        for i in range( n ):
            temp = []
            for j in range(i, -1, -1):
                if s[j:i+1] in wordDict and j in hashMap:
                    for item in hashMap[j]:
                        temp.append( (item + ' ' + s[j:i+1]).strip() )
            hashMap[i+1] = temp
        
        return hashMap[ n ]