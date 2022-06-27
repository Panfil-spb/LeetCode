# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        def elem(num, root):
            if len(res) >= num:
                res[num-1].append(root.val)
            else:
                res.append([root.val])
            if root.left:
                elem(num+1, root.left)
            if root.right:
                elem(num+1, root.right)
        
        if root:
            elem(1, root)
        
        return res
            
        