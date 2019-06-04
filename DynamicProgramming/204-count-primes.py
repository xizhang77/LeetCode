# -*- coding: utf-8 -*-

'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''
# Soluiton 1: LTE
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        hashMap = {2:0, 3:0, 5:0, 7:0 }
        
        p = 2
        while p < n:
            if p in hashMap:
                p += 1
                continue
            flag = 1
            for key in hashMap.keys():
                if p%key == 0:
                    hashMap[ key ] += 1
                    flag = 0
                    break
            if flag:
                hashMap[ p ] = 0
            p += 1
            
        return n - sum(hashMap.values()) - 2


# Solution 2: DP
# Check Line 60!!!
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        prime = [ 1 ] * n
        
        prime[0], prime[1] = 0, 0
        
        for i in range( 2, int(n **(0.5)) + 1):
            if prime[i]:
                prime[i*i: n: i] = [0] * ((n - 1) // i - i + 1) #[Faster than for loop]
        
        return sum( prime )
        