# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        
        ans = []
        if root == None:
            return []
        self.helper(root, [], root.val, targetSum, ans)
        return ans
        
    def helper(self, node, psf, tsf, target, ans):
        
        if(node.left == None and node.right == None):
            # leaf node
            if(tsf == target):
                psf.append(node.val)
                ans.append(copy.deepcopy(psf))
                psf.pop()
            return
        psf.append(node.val)
        if(node.left != None):
            self.helper(node.left, psf, tsf + node.left.val, target, ans)
        if(node.right != None):
            self.helper(node.right, psf, tsf + node.right.val, target, ans)
        psf.pop()
                
        
        