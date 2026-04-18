# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = defaultdict(bool) # this makes if check O(1)

        while head:
            if visited[head]:
                return True
            else:
                visited[head] = True
            head = head.next

        return False
        