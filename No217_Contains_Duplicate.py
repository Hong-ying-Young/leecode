#No.217_Contains_Duplicate
#Given an array of integers, find if the array contains any duplicates. 
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

#solution 1
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

#solution 2
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False