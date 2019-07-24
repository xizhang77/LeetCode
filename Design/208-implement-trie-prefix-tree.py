# -*- coding: utf-8 -*-

'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.child = []
        self.isWord = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TreeNode(None)
                
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.trie
        
        for char in word:
            flag = 1
            for node in p.child:
                if node.val == char:
                    flag = 0
                    p = node
                    break
            if flag:
                node = TreeNode( char )
                p.child.append( node )
                p = node
                
        p.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.trie
        
        for char in word:
            flag = 1
            for node in p.child:
                if node.val == char:
                    flag = 0
                    p = node
                    break
            if flag:
                return False
        
        return p.isWord
                

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.trie
        
        for char in prefix:
            flag = 1
            for node in p.child:
                if node.val == char:
                    flag = 0
                    p = node
                    break
            if flag:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)