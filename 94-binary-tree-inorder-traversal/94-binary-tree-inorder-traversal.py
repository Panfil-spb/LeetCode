# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self, root):
        mass = []
        if root is None:
            return []
        if root.left != None:
            for i in self.inorderTraversal(root.left):
                mass.append(i)
        mass.append(root.val)
        if root.right != None:
            for i in self.inorderTraversal(root.right):
                mass.append(i)
        
        return mass
        