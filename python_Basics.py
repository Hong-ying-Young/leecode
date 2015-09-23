#Python Algorithms book, chapter 2: Basics
#python Basics, try out thoese short basics and get a sense of python
num = [4,6,8,1]
num.append(1)
num.insert(0,1)

s = 0
for x in num:
	s +=x

square = [x**x for x in num]

s=0
for x in num:
	for y in num:
		s += x*y

seq1 = [[0, 1], [2], [3, 4, 5]] 
s=0
for seq2 in seq1:
	for x in seq2:
		s +=x
#to time your algorithm use timeit
improt timeit
timeit.timeit("x = 2+2")

#to find bottlenecks,use a profiler use module cProfile or profile
#This should print out timing results about the various functions in your program
import cProfile
cProfile.run('main()')

#plot performance, use box plots to show the distribution of running times

# a straightforward adjacency set representation
a, b, c, d, e, f, g, h = range(8) 
N=[
{b, c, d, e, f}, #a 
{c, e}, #b 
{d}, #c
{e}, #d 
{f}, #e
{c, g, h}, #f
{f, h}, #g
{f, g} #h
]

#adjacency lists
a, b, c, d, e, f, g, h = range(8) 
N=[
[b, c, d, e, f], #a 
[c, e], #b 
[d], #c
[e], #d 
[f], #e
[c, g, h], #f
[f, h], #g
[f, g] #h
]

#tips:deleting objects from the middle of a Python list is costly. Deleting from the end of a list takes constant time

#adjacency dicts with edge weights
a, b, c, d, e, f, g, h = range(8) 
N=[
{b:2, c:1, d:3, e:9, f:4}, #a 
{c:4, e:3}, #b 
{d:8}, #c
{e:7}, #d 
{f:5}, #e
{c:2, g:2, h:2}, #f
{f:1, h:6}, #g
{f:9, g:8} #h
]

#a dic with adjacency sets
N={
'a': set('bcdef'), 
'b': set('ce'), 
'c': set('d'), 
'd': set('e'), 
'e': set('f'), 
'f': set('cgh'), 
'g': set('fh'), 
'h': set('fg')
}

#adjacency matrices
a, b, c, d, e, f, g, h = range(8)
# abcdefgh
N = [[0,1,1,1,1,1,0,0], # a 
[0,0,1,0,1,0,0,0], # b 
[0,0,0,1,0,0,0,0], # c 
[0,0,0,0,1,0,0,0], # d 
[0,0,0,0,0,1,0,0], # e 
[0,0,1,0,0,0,1,1], # f 
[0,0,0,0,0,1,0,1], # g 
[0,0,0,0,0,1,1,0]] # h

#A Weight Matrix with Infinite Weight for Missing Edges

a, b, c, d, e, f, g, h = range(8)
_ = float('inf')
# abcdefgh
W = [[0,2,1,3,9,4,_,_], # a 
[_,0,4,_,3,_,_,_], # b 
[_,_,0,8,_,_,_,_], # c 
[_,_,_,0,7,_,_,_], # d
[_,_,_,_,0,5,_,_], # e 
[_,_,2,_,_,0,2,2], # f 
[_,_,_,_,_,1,0,6], # g 
[_,_,_,_,_,9,8,0]] # h

#special purpose arrays with NUMPY
N = [[0]*10 for i in range 10]

import numpy as np
N = np.zeros([10,10])

#implementing trees
T = [["a", "b"], ["c"], ["d", ["e", "f"]]]
T[0][1] #'b'
T[2][1][0] #'e'

#A Binary Tree Class
class Tree:
def __init__(self, left, right): 
	self.left = left
    self.right = right

t = Tree(Tree("a", "b"), Tree("c", "d"))
t.right.left #c

# A multiway tree class
class Tree:
	def __init__(self, kids, next=None):
		self.kids = self.val = kids
		 self.next = next

t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
t.kids.next.next.val  #c


class Bunch(dict):
	def __init__(self, *args, **kwds):
		super(Bunch, self).__init__(*args, **kwds) 
        self.__dict__ = self

x = Bunch(name="Jayne Cobb", position="Public Relations")
x.name  #'Jayne Cobb'

T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))
t.left
t['left']['right']
"left" in t.right
"right" in t.right

#Graph library: NetworkX, python-graph, Graphine

#looking for an element in a list
#Using a list would give you quadratic running time, whereas using a set would be linear.

from random import randrange
L = [randrange(10000) for i in range(1000)]
42 in L
S = set(L)
42 in L

#never compare floats for equality
sum(0.1 for i in range(10)) == 1.0   #False

def almost_equal(x, y, places=7): 
	return round(abs(x-y), places) == 0

#get exact decimal floating-point number
from decimal import *
sum(Decimal("0.1") for i in range(10)) == Decimal("1.0")  #True

sage: 3/5 * 11/7 + sqrt(5239)
13*sqrt(31) + 33/35
