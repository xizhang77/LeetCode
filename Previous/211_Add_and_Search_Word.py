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
                return self.dfs( word[1:], node.child[ word[0] ])
        else:
            for char in node.child:
                if self.dfs( word[1:], node.child[ char ]):
                    return True
            return False
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)