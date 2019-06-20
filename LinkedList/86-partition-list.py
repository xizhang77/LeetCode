# -*- coding: utf-8 -*-

'''
Given a linked list and a value x, partition it such that all nodes less than x 
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time & Space: O(n)
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = []
        great = []
        while head:
            if head.val < x:
                less.append( head )
            else:
                great.append( head )
            head = head.next

        node = ListNode( None )
        p = node
        while less:
            temp = less.pop(0)
            temp.next = None
            p.next = temp
            p = p.next
            
        while great:
            temp = great.pop(0)
            temp.next = None
            p.next = temp
            p = p.next
        
        
        return node.next