#http://www.toptal.com/python/interview-questions
#1. what will be the output of the code below and explain your answer
def extendList(val,list=[]):
   ....:     list.append(val)
   ....:     return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" %s list1
print "list2 = %s" %s list2
print "list3 = %s" %s list3

#aswer: list1 = [10,'a'], list2 = [123], list3 = [10,'a']

＃revise
def extendList(val,list=None):
	if list is None:
		list = []
		list.append(val)
		return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

#anser: list 1 = [10], list2 = [123], list3=['a']
#2
def multipliers():
    return [lambda x : i * x for i in range(4)]
    
print [m(2) for m in multipliers()]

#answer: [6,6,6,6]
#revise
def multipliers():
     for i in range(4): yield lambda x : i * x 

#answer: [0,2,4,6]

#3 

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

#anser: 1 1 1; 1 2 1; 3 2 3

#4
def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

#in python 2 the result is different form python3
#from __future__ import division 

#5 
list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

#6
list = [ [ ] ] * 5
list  # output?
list[0].append(10)
list  # output?
list[1].append(20)
list  # output?
list.append(30)
list  # output?

#the key thing to understand here is that the statement list = [ [ ] ] * 5 
#does NOT create a list containing 5 distinct lists; rather, it creates a 
#list of 5 references to the same list. 
#list[0].append(10) appends 10 to the first list. 
#But since all 5 lists refer to the same list, the output is: [[10], [10], [10], [10], [10]].

#In contrast, list.append(30) is appending an entirely new element to the “outer” list, 
#which therefore yields the output: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30].

#6: Given a list of N numbers, return a) even numbers and b) from elements in the original list
#that has even indices

[x for x in list[::2] if x%2==0]
#[x for x in list[::2] if x%2 == 0]

#7 given the following subclass of dictionary:
class DefaultDict(dict):
    def __missing__(self, key):
        return []
#will the code below work? why or why not?
d = DefaultDict()
d['florp'] = 127
