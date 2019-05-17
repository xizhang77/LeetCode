# -*- coding: utf-8 -*-
'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''


'''
两种做法
1.  定义两个队列，当需要push新元素时找到不为空的那个队列，
    需要pop元素时将不为空的那个队列的前n-1（n为不为空队列的长度）的元素弹出并插入为空的队列中，
    再pop最后一个元素。
    这样push的时间复杂度是O(1)，pop和top的时间复杂度为O(n)

2.  只使用一个队列，在每次push新元素后，将队列中前(n-1)个元素依次弹出并插入队尾，这样新插入的元素永远在队列的最前端。
    这样push的时间复杂度是O(n)，但pop和top的时间复杂度为O(1)

'''

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append( x )

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        
        return self.stack == []

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()