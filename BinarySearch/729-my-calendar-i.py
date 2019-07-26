# -*- coding: utf-8 -*-

'''
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
'''

# Binary Search
# Time: O(nlogn)
# Refer: https://leetcode.com/problems/my-calendar-i/discuss/109477/Binary-Search-Python-with-Explanations
class MyCalendar(object):

    def __init__(self):
        self.calendar = []
    
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        idx_s = bisect.bisect_right(self.calendar, start)
        
        if idx_s%2:
            return False
        idx_e = bisect.bisect_left(self.calendar, end)
        
        if idx_s != idx_e:
            return False
        
        self.calendar[idx_s:idx_e] = [start, end]
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# Time: O(n^2) where n is the # calls for func book
class MyCalendar(object):

    def __init__(self):
        self.calendar = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # print self.calendar
        
        for key in self.calendar:
            if key <= start < self.calendar[ key ] or ( start < key < end ):
                return False
        
        self.calendar[ start ] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)