# -*- coding: utf-8 -*-

'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The following solutions are similar to #102.

# Recursive
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
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs( root, 0, ans )
        
        return ans[::-1]

# Recursive [Using a hashMap instead of reverse the answer ]
class Solution(object):
    def dfs(self, node, level, ans):
        if not node:
            return
        
        self.dfs( node.left, level + 1, ans )
        self.dfs( node.right, level + 1, ans )
        
        if level not in ans:
            ans[ level ] = [ node.val ]
        else:
            ans[ level ] += [ node.val ]
        
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = {}
        
        self.dfs( root, 0, ans )
        
        return [ ans[key] for key in sorted(ans.keys(), reverse = True)]

# Iterative 
class Solution(object):
    def levelOrderBottom(self, root):
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
            
            ans = [ value ] + ans
            current = nextLevel
        
        return ans