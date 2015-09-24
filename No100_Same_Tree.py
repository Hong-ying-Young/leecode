#No.100_Same_Tree
#Given two binary trees, write a function to check if they are equal or not.
#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False