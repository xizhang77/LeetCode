# -*- coding: utf-8 -*-

'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# [Recursive, retrival whole tree] Runtime: 36 ms, faster than 11.15% of Python online submissions for Same Tree.
class Solution1(object):
    def retrival(self, root, ans):
        if not root:
            ans.append( "null" )
            return
        ans.append( root.val )
        self.retrival( root.left, ans )
        self.retrival( root.right, ans )
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ansP = []
        ansQ = []
        
        self.retrival( p, ansP )
        self.retrival( q, ansQ )
        
        return ansP == ansQ

# [Recursive with pruning] Runtime: 20 ms, faster than 79.01% of Python online submissions for Same Tree.
class Solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        if (not p) or (not q):
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree( p.left, q.left ) and self.isSameTree( p.right, q.right ) 

# [Iterative with Stack] Runtime: 20 ms, faster than 79.01% of Python online submissions for Same Tree.
class Solution3(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [ [p, q] ]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if (not node1) or (not node2):
                return node1 == node2
            if node1.val != node2.val:
                return False
            
            stack.append( [node1.left, node2.left] )
            stack.append( [node1.right, node2.right] )
        
        return True