# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = TreeNode()
        if root1 is None and root2 is None:
            return None
        if root1:
            root.val += root1.val
        if root2:
            root.val += root2.val
        
        if root1 and root2:
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            root.left = root1.left
            root.right = root1.right
        elif root2:
            root.left = root2.left
            root.right = root2.right
        return root
        