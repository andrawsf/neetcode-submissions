# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            reverse = ListNode(head.val)
        else: 
            return None

        while head.next:
            #print("old head ", reverse.val, " new head ", head.next.val)
            reverse = ListNode(head.next.val, reverse)
            head = head.next

        return reverse