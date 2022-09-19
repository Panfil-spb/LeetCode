# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse(p, q):
            if p is None and q is None:
                return 1
            if p is None or q is None:
                return 0
            if p.val != q.val:
                return 0
            return traverse(p.left, q.right) and traverse(p.right, q.left)

        return traverse(root.left, root.right)