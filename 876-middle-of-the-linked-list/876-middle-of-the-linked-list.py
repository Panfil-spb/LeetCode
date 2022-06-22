# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = mid = head
        
        count = 0
        
        while curr.next is not None:
            curr = curr.next
            if count % 2 == 0:
                count += 1
                mid = mid.next
            else:
                count += 1
        return mid