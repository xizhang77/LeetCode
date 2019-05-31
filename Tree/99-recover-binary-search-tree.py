# -*- coding: utf-8 -*-

'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
Refer: https://blog.csdn.net/fuxuemingzhu/article/details/79672901
'''

class Solution(object):
    def inOrder(self, root):
        if not root:
            return
        
        self.inOrder( root.left )
        
        if self.prev and self.prev.val > root.val:
            if not self.node1:
                self.node1 = self.prev
            self.node2 = root
            
        self.prev = root  
        self.inOrder( root.right )
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev, self.node1, self.node2 = None, None, None
        self.inOrder( root )
        
        self.node1.val, self.node2.val = self.node2.val, self.node1.val