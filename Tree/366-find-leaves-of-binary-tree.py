# -*- coding: utf-8 -*-

'''
Given a binary tree, collect a tree's nodes as if you were doing this: 
Collect and remove all leaves, repeat until the tree is empty.

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, parent):
        self.relation[ node ] = [ parent, 0 ]
        if node.left:
            self.relation[ node ][-1] += 1
            self.dfs( node.left, node )
        if node.right:
            self.relation[ node ][-1] += 1
            self.dfs( node.right, node )
        
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        self.relation = {}
        self.dfs( root, None )
        
        ans = [ ]
        
        while self.relation:
            temp = []
            delete = []
            for node in self.relation:
                if self.relation[ node ][-1] == 0:
                    temp.append( node.val )
                    delete.append( node )
            for node in delete:
                parent = self.relation[ node ][0]
                if parent in self.relation:
                    self.relation[ parent ][-1] -= 1
                del self.relation[ node ]
            ans.append( temp )
        return ans