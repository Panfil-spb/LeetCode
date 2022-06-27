"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def elem(children):
            for i in children:
                res.append(i.val)
                elem(i.children)
                
        res = []
        if root:
            res.append(root.val)
            elem(root.children)
        
        
        
        return res
        