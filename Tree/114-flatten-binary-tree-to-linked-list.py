# -*- coding: utf-8 -*-

'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time and Space: O(n)
class Solution1(object):
    def dfs(self, root):
        if not root:
            return
        
        if not root.left and not root.right:
            return root, root
        elif not root.left and root.right:
            start, end = self.dfs( root.right )
            return root, end
        elif root.left and not root.right:
            start, end = self.dfs( root.left )
            root.left = None
            root.right = start
            return root, end
        else:
            ls, le = self.dfs( root.left )
            rs, re = self.dfs( root.right )
            root.left = None
            root.right = ls
            le.right = rs
            return root, re
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.dfs( root )


# [More elegant way based on preorder traversal]
class Solution2(object):
    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten( root.right )
        self.flatten( root.left )
        
        root.right = self.prev
        root.left = None
        self.prev = root

# [Updated Solution 1 based on preorder traversal ]
class Solution3(object):
    def dfs(self, root):
        if not root:
            return
        self.dfs( root.right )
        self.dfs( root.left )
        
        root.left = None
        root.right = self.prev
        self.prev = root
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        
        self.dfs( root )