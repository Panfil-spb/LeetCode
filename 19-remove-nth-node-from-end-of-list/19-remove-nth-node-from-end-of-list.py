# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        if count == 1 or count == n:
            return head.next
        
        curr = slow = head
        while curr:
            if count == n:
                slow.next = curr.next
                return head
            else:
                count -= 1
                slow = curr
                curr = curr.next
        return head
                
        
        