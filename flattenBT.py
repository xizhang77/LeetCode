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

class Solution(object):
    def preOrder(self, root, stack):
        if not root:
            return
        stack.append(root)
        self.preOrder( root.left, stack )
        self.preOrder( root.right, stack )
    
    def retrival(self, root, stack):
        if not stack:
            return
        root = stack.pop(0)
        root.left = None
        root.right = stack[0] if stack else None
        self.retrival( root.right, stack )
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        self.preOrder( root, stack )
                      
        self.retrival( root, stack )