# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ls2 = l2
        prev = curr = head = l1
        while curr is not None:
            
            if curr is not None and ls2 is not None:
                num = curr.val + ls2.val
                if num < 10:
                    curr.val = num
                else:
                    curr.val = num % 10
                    if curr.next is not None:
                        curr.next.val += num // 10
                    else:
                        curr.next = ListNode(num // 10)
            
                if curr.next is None and ls2.next is not None:
                    curr.next = ls2.next
                    break
                else:
                    curr = curr.next
                ls2 = ls2.next
                
            elif ls2 is None:
                num = curr.val
                if num < 10:
                    curr.val = num
                else:
                    curr.val = num % 10
                    if curr.next is not None:
                        curr.next.val += num // 10
                    else:
                        curr.next = ListNode(num // 10)
                
                curr = curr.next
                        
     
        return head    
                    
        