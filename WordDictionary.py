# -*- coding: utf-8 -*-
'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''

class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[ char ] = TrieNode()
            node = node.child[ char ]
        node.isWord = True

    def dfs(self, word, node):
        if not node:
            return False
        if not word:
            return node.isWord

        if word[0] != '.':
            if word[0] not in node.child:
                return False
            else:
                return self.dfs( word[1:], node.child[ word[0]] )
        else:
            for char in node.child:
                if self.dfs( word[1:], node.child[char]):
                    return True
            return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs( word, self.root)

obj = WordDictionary()
'''
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')

print obj.search("pad")
print obj.search("bad")
print obj.search(".ad")
print obj.search("b..")
'''

obj.addWord('a')
obj.addWord('a') 

# print obj.search(".")
print obj.search("a")
print obj.search("aa")
print obj.search(".a")
print obj.search("a.")


'''
["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
'''
