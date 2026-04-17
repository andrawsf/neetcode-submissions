# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        reverse = None

        while head:
            #print("old head ", reverse.val, " new head ", head.next.val)
            reverse = ListNode(head.val, reverse)
            head = head.next

        return reverse