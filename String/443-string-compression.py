# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/string-compression/
'''


# Time: O(n); Space: O(1)
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        ans = len( chars )
        
        while i < ans:
            if i + 1 < ans and chars[i] == chars[ i + 1 ]:
                count = 2
                i += 1
                while i + 1 < ans and chars[ i ] == chars[ i+1 ]:
                    chars.pop( i+1 )
                    count += 1
                    ans -= 1
                temp = str(count)
                lens = len( temp )
                if lens == 1:
                    chars[ i ] = temp
                else:
                    chars[ i ] = temp[0]
                    for j in temp[1: ]:
                        chars.insert(i+1, j)
                        ans += 1
                        i += 1
            i += 1
        
        return ans