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

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.child = []
        self.isWord = False
        
class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TreeNode( None )
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        p = self.trie
        for char in word:
            flag = 1
            for node in p.child:
                if node.val == char:
                    p = node
                    flag = 0
                    break
            if flag:
                newnode = TreeNode( char )
                p.child.append( newnode )
                p = newnode
        p.isWord = True
        
    def dfs(self, word, root):
        if not word:
            return root.isWord
        
        if word[0] == '.':
            for node in root.child:
                if self.dfs( word[1:], node ):
                    return True
        else:
            for node in root.child:
                if node.val == word[0]:
                    return self.dfs( word[1:], node )
            
        return False
            
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs( word, self.trie )


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)