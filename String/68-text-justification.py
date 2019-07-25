# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/text-justification/
'''

# Time: O(n*m) while n = len(words) and m = max(len(word) for word in words)
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        groups = []
        
        n = len(words)
        i = 0
        while i < n:
            count = 0
            temp = []
            while i < n and count + len( words[i] ) <= maxWidth:
                temp.append( words[i] )
                count += len( words[i] ) + 1
                i += 1
            groups.append( temp )
        
        ans = []
        for i, group in enumerate(groups):
            c_word = len(group)
            c_char = sum( len(word) for word in group )    
            temp = group
            
            if i == len(groups) - 1:
                ans.append( " ".join(temp) + " "*(maxWidth - c_char - c_word + 1 ) )
            elif c_word == 1:
                ans.append( "".join(temp) + " "*(maxWidth - c_char) )
            else:
                count = maxWidth - c_char
                idx = []
                for j in range( c_word - 1 ):
                    idx.append( j*2+1 )
                    temp.insert(j*2+1, " ")
                    count -= 1
                k = 0
                while count > 0:
                    temp[ idx[k] ] += " "
                    k = (k+1)%len(idx)
                    count -= 1
                ans.append( "".join(temp) )
        return ans