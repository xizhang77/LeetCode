# -*- coding: utf-8 -*-

'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [Iterative]
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        ans = []
        
        if not root:
            return ans
        
        stack = [ [root, 0] ]

        while stack:
            node, check = stack[-1]
            if check:
                ans.append( node.val )
                stack.pop()
                continue
                
            stack[-1][1] = 1
            if node.right:
                stack.append( [node.right, 0] )
            if node.left:
                stack.append( [node.left, 0] )
            
        return ans