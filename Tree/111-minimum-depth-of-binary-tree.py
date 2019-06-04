# -*- coding: utf-8 -*-

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
# Time: O(n); Space: O(logn)
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        level = [ root ]
        ans = 1
        while level:
            nextlevel = []
            for node in level:
                if not node.left and not node.right:
                    return ans
                if node.left:
                    nextlevel.append( node.left )
                if node.right:
                    nextlevel.append( node.right )
            level = nextlevel
            ans += 1
        
