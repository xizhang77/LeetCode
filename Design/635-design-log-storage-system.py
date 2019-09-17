# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/design-log-storage-system/
'''

class LogSystem(object):

    def __init__(self):
        self.list = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        time = timestamp.split(":")
        time = "".join(time)
        self.list.append( [time, id] )
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        granularity = {'Year':4, 'Month':6, 'Day':8, 'Hour':10, 'Minute':12, 'Second': 14}
        
        start, end = "".join(s.split(":")), "".join(e.split(":"))
        
        start = int(start[:granularity[gra]] )
        end = int( end[:granularity[gra]] )
        
        self.list.sort( key=lambda x:x[0])
        
        ans = []
        
        for i in range( len(self.list) ):
            temp = int( self.list[i][0][:granularity[gra]] )
            if int( temp ) < start:
                continue
            elif start <= temp <= end:
                ans.append( self.list[i][1] )
            else:
                break
        
        return ans
                


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)