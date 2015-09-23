#No.266 Palindrome Permutation 
#Given a string S, determine if a permutation of the string could form a palindrome.
#For example,"code" -> False, "aab" -> True, "carerac" -> True.
# check that there's at most one character with an odd number of occurrences

from collections import Counter

    def canMakePalindrom(s):
    return len([v for v in Counter(s).values() if v % 2 == 1]) <= 1

#Or:

class Solution:
	from collections import Counter
	def canMakePalindrom(s):
	return sum(v %2 ==1 for v in Counter(s).values()) <=1