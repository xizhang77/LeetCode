
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Space: O(n)

class Solution(object):
    def dfs(self, root, path, ans, sum):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            ans.append( path + [ root.val ])
            return

        self.dfs( root.left, path + [ root.val ], ans, sum - root.val )
        self.dfs( root.right, path + [ root.val ], ans, sum - root.val )
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        
        self.dfs( root, [], ans, sum )
        
        return ans