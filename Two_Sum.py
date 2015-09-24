#Two_Sum
#Given an array of integers, find two numbers such that they add up to a specific target number.
#The function twoSum should return indices of the two numbers such that they add up to the target, 
#where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#You may assume that each input would have exactly one solution.
#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2
#解题思路：1，由于要找到符合题意的数组元素的下标，所以先要将原来的数组深拷贝一份，然后排序。

#　　　　   2，然后在排序后的数组中找两个数使它们相加为target。这个思路比较明显：使用两个指针，一个指向头，一个指向尾，两个指针向中间移动并检查两个指针指向的数的和是否为target。如果找到了这两个数，再将这两个数在原数组中的位置找出来就可以了。

#　　　　3，要注意的一点是：在原来数组中找下标时，需要一个从头找，一个从尾找，要不无法通过。如这个例子：numbers=[0,1,2,0]; target=0。如果都从头开始找，就会有问题。

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i