# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        
        slow, curr = head, head
        
        while curr:
            if curr.val == val:
                slow.next = curr.next
                curr = curr.next
            else:
                slow = curr
                curr = curr.next
        return head
                
        