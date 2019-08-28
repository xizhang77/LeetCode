# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/serialize-and-deserialize-bst/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def dfs(self, root, path):
        if not root:
            return
        path.append( str( root.val ) )
        self.dfs( root.left, path )
        self.dfs( root.right, path )
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        self.dfs( root, path )
        
        return "/".join( path )
    
    def solver(self, nums ):
        if not nums:
            return
        val = nums.pop(0)
        node = TreeNode( val )
        
        i = 0
        while i < len(nums):
            if nums[i] > val:
                break
            i += 1
        
        node.left = self.solver( nums[:i])
        node.right = self.solver( nums[i:] )
        
        return node
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nums = data.split("/")
        nums = [ int(num) for num in nums ]
        return self.solver( nums )
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))