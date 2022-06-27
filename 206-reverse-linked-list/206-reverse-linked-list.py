# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = ListNode(head.val, None)
        head = head.next
        while head:
            curr = ListNode(head.val, curr)
            head = head.next
        return curr
        