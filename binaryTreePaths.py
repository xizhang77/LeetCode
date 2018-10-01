# -*- coding: utf-8 -*-
'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, path, ans):
        if not root:
            return
        if not root.left and not root.right:
            temp = path + [str(root.val)]
            temp = "->".join(temp)
            ans.append(temp)
            return
        self.dfs( root.left, path + [str(root.val)], ans)
        self.dfs( root.right, path + [str(root.val)], ans)
            
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        self.dfs( root, [], ans)
        
        return ans