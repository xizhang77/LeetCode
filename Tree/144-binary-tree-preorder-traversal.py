# -*- coding: utf-8 -*-

'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1: Recursively
class Solution(object):
    def preOrder(self, root, ans):
        if not root:
            return
        ans.append( root.val )
        self.preOrder( root.left, ans )
        self.preOrder( root.right, ans )
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        self.preOrder( root, ans )
        
        return ans


# Solution 2: Iteratively
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        if not root:
            return ans
        
        temp = [ root ]
        
        while temp:
            node = temp.pop()
            ans.append( node.val )
            if node.right:
                temp.append( node.right )
            if node.left:
                temp.append( node.left )
        
        return ans