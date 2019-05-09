# -*- coding: utf-8 -*-

'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Time & Space: O(n)

# [BFS, Iterative]
class Solution1(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        
        if not root:
            return ans
        
        current = [ root ]
        flag = 0
        while current:
            value = []
            nextLevel = []
            for node in current:
                value.append( node.val )
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )
            if flag:
                value = value[::-1]
            
            ans.append( value )
            current = nextLevel
            flag = 1 - flag
        
        return ans

# [DFS, Recursive]
class Solution2(object):
    def dfs(self, root, level, ans):
        if not root:
            return
        if len(ans) - 1 < level:
            ans.append( [root.val] )
        else:
            if level%2:
                ans[ level ] = [ root.val ] + ans[ level ]
            else:
                ans[ level ].append( root.val )
        
        self.dfs( root.left, level + 1, ans )
        self.dfs( root.right, level + 1, ans )
        
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( root, 0, ans )
        
        return ans