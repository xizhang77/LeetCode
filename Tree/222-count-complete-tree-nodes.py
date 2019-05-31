# -*- coding: utf-8 -*-

'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N)
# Space: O(logN)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        count = 0
        
        if not root:
            return count
        
        curr = [ root ]
        level = 0
        
        while True:
            if len( curr ) != 2**level:
                count += len( curr )
                return count
            
            count += 2**level
            nextLevel = []
            
            for node in curr:
                if node.left:
                    nextLevel += [ node.left ]
                if node.right:
                    nextLevel += [ node.right ]
            curr = nextLevel 
            level += 1
