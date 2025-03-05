class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root, L, R):
        a = root.val
        if L == R == a:
            self.sum += a
        elif L < R and (a >= L and a <=R):
            self.sum += a
        elif L > R and (a <= L and a >= R):
            self.sum += a

        if root.left:
            self.rangeSumBST(root.left, L, R)

        if root.right:
            self.rangeSumBST(root.right, L, R)

        return self.sum


s = Solution()

rr1 = TreeNode(18)
rl1 = TreeNode(None)
lr1 = TreeNode(7)
ll1 = TreeNode(3)


r1 = TreeNode(15)
r1.left = rl1
r1.right = rr1


l1 = TreeNode(5)
l1.left = ll1
l1.right = lr1

root = TreeNode(10)
root.left = l1
root.right = r1


print (s.rangeSumBST(root, 15, 7))


""" 
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.
 
Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 
Note:
	1. The number of nodes in the tree is at most 10000.
	2. The final answer is guaranteed to be less than 2^31.
      10
      /    \
    5      15
  / \      / \
 3  7    n  18
       10
      /    \
    5      15
  / \      / \
 3  7    n  18
 /\  /\  /\  /\
1 n 6  n n n n
"""
