# -*- coding: utf-8 -*-

'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self, nums):
        if not nums:
            return None
        idx = len(nums)/2
        root = TreeNode( nums[idx] )
        root.left = self.inOrder( nums[:idx])
        root.right = self.inOrder( nums[idx+1:])
        
        return root
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return []
        nums = []
        while head:
            nums.append( head.val )
            head = head.next
        print nums
        return self.inOrder( nums )