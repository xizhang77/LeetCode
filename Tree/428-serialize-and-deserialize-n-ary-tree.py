# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    def dfs(self, root ):
        if not root:
            return ""
        path = []
        for node in root.children:
            path.append( self.dfs( node ) )
            
        if path:
            return str( root.val ) + " [ " + " ".join(path) + " ] "
        else:
            return str( root.val ) 
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        ans = self.dfs( root )
        # print ans
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """        
        if not data:
            return
        
        path = data.split(" ")
        
        root = Node( int( path.pop(0) ), [] )
        
        stack = [ [root, []] ]
        for val in path:
            if val == '[':
                if stack[-1][1]:
                    node = stack[-1][1][-1]
                    stack.append([node, []])
            elif val == ']':
                stack[-1][0].children = stack[-1][1]
                stack.pop()
            elif val.isdigit():
                node = Node( int(val), [] )
                stack[-1][1].append( node )
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))