# -*- coding: utf-8 -*-

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time & Space [For both solutions] O(n)

# [Solution 1: Recursive]
class Solution1(object):
    def dfs(self, root, level ):
        if not root:
            return level
        return max(self.dfs( root.left, level + 1), self.dfs( root.right, level + 1))
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs( root, 0 )


# [Solution 2: Iterative]
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        
        if not root:
            return level
        
        current = [ root ]
        
        while current:
            level += 1
            nextLevel = []
            for node in current:
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )
            current = nextLevel
        
        return level