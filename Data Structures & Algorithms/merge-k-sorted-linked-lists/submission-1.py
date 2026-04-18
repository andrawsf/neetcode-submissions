# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        
        # could just do 2 at a time
        while len(lists) > 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            sorted = ListNode()
            newlist = sorted

            while list1 and list2:
                #print('Comp',list1.val," w ",list2.val)
                if list1.val < list2.val: 
                    sorted.next = list1
                    list1 = list1.next
                    sorted = sorted.next
                else:
                    sorted.next = list2
                    list2 = list2.next
                    sorted = sorted.next

            #now only one list remains
            if list1:
                sorted.next = list1
            elif list2:
                sorted.next = list2
        
            # now push this list back:
            lists.append(newlist.next)\
            #print("next lists")

        return lists[0]

                

