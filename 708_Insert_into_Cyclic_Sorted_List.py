"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        node = Node(insertVal, None)
        if not head:
            node.next = node
            return node
        
        if not head.next:
            node.next = head
            head.next = node
            return head
        
        p = head.next
        
        check = []
        while p != head:
            if p.val < insertVal and p.next.val >= insertVal:
                break
            if p.val > p.next.val:
                check = [[p.next.val, p.next], [p.val, p]] #Get the min and max
            p = p.next
        
        if check and (insertVal <= check[0][0] or insertVal >= check[1][0]):
            front, end = check[0][1], check[1][1]
            end.next = node
            node.next = front
        else:
            end, front = p, p.next
            end.next = node
            node.next = front
        
        return head
            