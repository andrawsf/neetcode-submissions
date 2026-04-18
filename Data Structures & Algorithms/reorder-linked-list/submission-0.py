# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        while head:
            nodes.append(head)
            head = head.next
        
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            nodes[i].next.next = nodes[i+1]
            i += 1
            j -= 1
        nodes[i].next = None
        
        return