#Python Algorithms book, chapter 3:Counting
x*sum(S) == sum(x*y for y in S)

#We’ve just seen that summing up the powers of two, 
#you always get one less than the next power of two. For example, 1 + 2 + 4 = 8 – 1, or 1 + 2 + 4 + 8 = 16 – 1
#a perfectly balanced binary tree has n –1 internal nodes.
#for a perfectly balanced binary tree, if n is the total nodes, then
#the hight of a tree h = log(n), the width (the number of leaves) n=2**h
log(n,2)

#check is a number a prime
def is_prime(n):
	for i in range(2,n):
		    if n % i == 0: return False 
    return True


def S(seq, i=0):
    if i == len(seq): return 0 
    return S(seq, i+1) + seq[i]

def T(seq, i=0):
    if i == len(seq): return 1 
    return T(seq, i+1) + 1

seq = range(1,101)
S(seq)  #5050
T(seq) #101

#Gnome sort, and sorting Algorithms

def gnomesort(seq): 
	i=0
    while i < len(seq):
    	if i == 0 or seq[i-1] <= seq[i]:
    		i += 1 else:
    		seq[i], seq[i-1] = seq[i-1], seq[i] 
    		i -= 1
#merge sort, another example sorting algorithm
def mergesort(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft) 
    if len(rgt) > 1: rgt = mergesort(rgt) 
    res = []
    while lft and rgt:
    	if lft[-1] >= rgt[-1]: 
    		res.append(lft.pop())
    	else: 
    		res.append(rgt.pop())
    res.reverse()
	return (lft or rgt) + res
	





