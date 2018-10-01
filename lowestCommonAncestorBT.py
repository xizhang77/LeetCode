# -*- coding: utf-8 -*-
'''
LTE... Try another way...
'''

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preOrder(self, root, p, q, path, ans):
        if not root or len(ans) == 2:
            return 
        if root == p:
            ans.append( path + [root] )
        if root == q:
            ans.append( path + [root] )
        self.preOrder(root.left, p, q, path + [root] , ans )
        self.preOrder(root.right, p, q, path + [root] , ans )
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = []
        self.preOrder( root, p, q, [], ans)
        if len(ans[0]) > len(ans[1]):
            ans = ans[::-1]
        # Idx = [ idx for idx in range(len(ans[0])) if ans[0][idx] == ans[1][idx] ]
        return ans[0][Idx[-1]]