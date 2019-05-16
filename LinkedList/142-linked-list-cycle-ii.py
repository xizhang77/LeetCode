# -*- coding: utf-8 -*-

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
首先用slow，fast双指针判断是否有cycle；

假设Head到环起点的长度为n，环部分的长度为m（list总长m+n）,假设slow和fast走到第t步相遇
那么相遇的情况为：（t-n)%m + n = (2*t-n)%m + n, 可以得到: t%m = 0
因此让finder和slow一个从起点一个从相遇点继续走，再走n步就会相遇（ (t+n)%m = n ）
而这时finder刚好走到环的起点
'''

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = finder = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                while slow != finder:
                    finder = finder.next
                    slow = slow.next
                return finder
        
        return None