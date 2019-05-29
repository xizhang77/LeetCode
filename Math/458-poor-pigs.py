# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/poor-pigs/

Refer: https://blog.csdn.net/lym940928/article/details/81096640
题目思路 
对于这道题，很像以前的一个国王要求奴隶尝酒并找出毒酒一样。
区别在于，这道题有喝完的死亡时间以及需要在规定的时间内完成检测，因此在这道题中，猪猪就可以重复利用： 
假如一头猪在15分钟内喝完毒药会死，但是因为一共有1个小时的时间，因此，在这一个小时中，猪一共可以尝4个桶，
既一头猪可以负责探测出5个桶是否有毒（如果只有5个桶，猪猪喝其中4个都没事儿，那问题就出在第五个）。 因此，
两头猪就可以负责5 * 5 = 25个桶的水
3头猪就可以负责5 * 5 * 5 = 125个桶的水（可以想象为一个立方的矩阵），
依次类推。
'''

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        ans = 0
        
        while ( (minutesToTest/minutesToDie + 1) ** ans < buckets):
            ans += 1
        
        return ans