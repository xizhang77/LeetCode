# -*- coding: utf-8 -*-

'''
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if not root:
            return 0, 0
        
        l_inc, l_dec = self.dfs( root.left )
        r_inc, r_dec = self.dfs( root.right )
        
        inc_len = dec_len = 1
        
        if root.left:
            if root.left.val == root.val + 1:
                dec_len = max( dec_len, l_dec + 1 )
            elif root.left.val == root.val - 1:
                inc_len = max( inc_len, l_inc + 1 )
        if root.right:
            if root.right.val == root.val + 1:
                dec_len = max( dec_len, r_dec + 1 )
            elif root.right.val == root.val - 1:
                inc_len = max( inc_len, r_inc + 1 )
        
        self.ans = max(self.ans, inc_len + dec_len - 1)
        return inc_len, dec_len
        
        
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        self.dfs( root )
        
        return self.ans