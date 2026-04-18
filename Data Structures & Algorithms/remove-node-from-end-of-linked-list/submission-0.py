# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pos = 0
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # increment right n steps forward
        while n > 0: 
            right = right.next
            n -= 1

        # now shift the window all the way
        while right:
            right = right.next
            left = left.next
        #print("Currently at ",dummy.val)
        
        # now break the link
        left.next = left.next.next
            
        return dummy.next