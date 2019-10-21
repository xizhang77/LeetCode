# -*- coding: utf-8 -*-

'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''

# Time and Space: O(n*m)
# n: len(words); m: max( len(word[i]) )
from collections import defaultdict
class Solution(object):
    def addEdge(self, word1, word2, graph, total):
        m, n = len(word1), len(word2)
        i = j = 0
        while i < m and j < n:
            if word1[i] != word2[j]:
                graph[ word2[j] ].append( word1[i] )
                break
            i += 1
            j += 1
            
    
    def dfs(self, graph, visited, char, ans):
        if visited[ char ] == 1:
            return False
        if visited[ char ] == 2:
            return True
        
        visited[ char ] += 1
        for j in graph[ char ]:
            if not self.dfs( graph, visited, j, ans ):
                return False
        
        visited[ char ] += 1
        ans += [ char ]
        
        return True
            
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict( list )
        total = words[0]
        for i in range( len(words) - 1):
            total += words[i+1]
            self.addEdge( words[i], words[i+1], graph, total )
        
        n = len( set(total) )
        char = list( set(total) )
        visited = defaultdict( int )
        
        ans = []
        for i in range( n ):
            if not self.dfs( graph, visited, char[i], ans):
                return ""
        
        return "".join(ans)