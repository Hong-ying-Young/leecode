#No. 104 Maximum Depth of Binary Tree
#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max( self.maxDepth(root.left), self.maxDepth(root.right) ) + 1