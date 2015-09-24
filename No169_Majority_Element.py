#No.169_Majority_Element
#Given an array of size n, find the majority element. 
#The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate, count = None, 0
        for e in num:
            if count == 0:
                candidate, count = e, 1
            elif e == candidate:
                count += 1
            else:
                count -= 1
        return candidate