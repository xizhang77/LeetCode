'''
Implement on LeetCode directly since it has predefined functions.

If implementing from scratch, 'izip_longest(a, b)' from package itertools also works.
'''

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = list(izip_longest(v1, v2))

    def next(self):
        """
        :rtype: int
        """
        subset = self.queue.pop(0)
        return x for x in subset if x is not None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue
        