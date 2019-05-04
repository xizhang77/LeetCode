# -*- coding: utf-8 -*-
'''
LTE... Try another way...
'''

'''
Given a list accounts, each element accounts[idx] is a list of strings, where the first element accounts[idx][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.


Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
'''

class Solution(object):
	def accountsMerge(self, accounts):
		"""
		:type accounts: List[List[str]]
		:rtype: List[List[str]]
		"""
		ans = []
		name = {}

		if not accounts:
			return ans
		while accounts:
			item = accounts.pop(0)
			item[1:] = sorted(set(item[1:]))
			print item
			if item[0] not in name:
				ans.append( item )
				name[ item[0] ] = [ans.index( item )]
			else:
				idxList = name[ item[0] ]
				candiList = []
				for idx in idxList:
					if set(ans[idx][1:] ) - (set(ans[idx][1:] ) - set( item[1:] )):
						candiList.append( idx )

				print 'Have to merge:', candiList

				if candiList:
					temp = []
					for i in range(len(candiList)):
						temp +=  ans[candiList[i]][1: ]
					print "duplicate terms", temp

					minIdx = candiList.pop(0)
					ans[minIdx][1:] = sorted(set( temp + item[1:] ))

					removeList = candiList
					print "remove", removeList


					if removeList:
						for remove in removeList:
							ans[remove] = []
						name[ item[0] ] = list( set(name[ item[0] ]) - set(removeList) )

				else:
					ans.append( item )
					name[ item[0] ].append( ans.index(item) )

			print name, ans

		return [ item for item in ans if item ]

obj = Solution()
# print obj.accountsMerge( [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]] )

print obj.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])