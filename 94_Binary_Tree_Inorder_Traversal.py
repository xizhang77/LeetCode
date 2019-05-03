# -*- coding: utf-8 -*-

'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Method 1: Recursive

class Solution1(object):
    def inOrder(self, root, ans):
        if not root:
            return
        self.inOrder( root.left, ans )
        ans.append( root.val )
        self.inOrder( root.right, ans )
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        self.inOrder( root, ans )
        
        return ans   

# Method 2: Iterative
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        
        while root or stack:
            while root:
                stack.append( root )
                root = root.left
            
            root = stack.pop()
            ans.append( root.val )
            root = root.right
        
        return ans    