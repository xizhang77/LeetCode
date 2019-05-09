# -*- coding: utf-8 -*-

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [BFS, Iterative] Time: O(n); Space: O(lgn)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        
        if not root:
            return ans
        
        current = [ root ]
        
        while current:
            value = []
            nextLevel = []
            
            for node in current:
                value.append( node.val )
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )
            
            ans.append( value )
            current = nextLevel
        
        return ans


# [DFS, Recursive] Time: O(n); Space: O(n)
class Solution(object):
    def dfs(self, node, level, ans):
        if not node:
            return
        if len(ans) - 1 < level:
            ans.append( [ node.val ] )
        else:
            ans[level].append( node.val )
        
        self.dfs( node.left, level + 1, ans )
        self.dfs( node.right, level + 1, ans )
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs( root, 0, ans )
        
        return ans