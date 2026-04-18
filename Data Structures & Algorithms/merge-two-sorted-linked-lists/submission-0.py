# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted = None

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    sorted = ListNode(list1.val, sorted)
                    list1 = list1.next
                else:
                    sorted = ListNode(list2.val, sorted)
                    list2 = list2.next
            elif list1:
                sorted = ListNode(list1.val, sorted)
                list1 = list1.next
            elif list2:
                sorted = ListNode(list2.val, sorted)
                list2 = list2.next

        # this is backwards so.... 
        reverseSorted = None
        while sorted:
            reverseSorted = ListNode(sorted.val, reverseSorted)
            sorted = sorted.next
        
        return reverseSorted


