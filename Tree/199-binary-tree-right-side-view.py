# -*- coding: utf-8 -*-

'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1: Iteratively
class Solution1(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        if not root:
            return ans
        
        stack = [ root ]
        
        while stack:
            nextLevel = []
            ans.append( stack[-1].val )
            for node in stack:
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )
            stack = nextLevel
        
        return ans


# Solution 2: Recursively

from collections import OrderedDict

class Solution2(object):
    def dfs(self, root, stack, level):
        if not root:
            return
        
        if level not in stack:
            stack[ level ] = root.val
        
        self.dfs( root.right, stack, level + 1)
        self.dfs( root.left, stack, level + 1)
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = OrderedDict()
        
        self.dfs( root, stack, 0 )
        
        return stack.values()
