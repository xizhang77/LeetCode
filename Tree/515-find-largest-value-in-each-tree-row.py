# -*- coding: utf-8 -*-

'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        if not root:
            return ans
        
        current = [ root ]
        
        while current:
            nextlevel = []
            temp = []
            for node in current:
                temp.append( node.val )
                if node.left:
                    nextlevel.append( node.left )
                if node.right:
                    nextlevel.append( node.right )
            ans.append( max(temp) )
            current = nextlevel
        
        
        return ans