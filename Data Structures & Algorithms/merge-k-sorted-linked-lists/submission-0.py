# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = head = ListNode()

        while(list1 and list2):
            if(list1.val < list2.val):
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if(list1):
            curr.next = list1
        if(list2):
            curr.next = list2

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if(n == 0):
            return None
        result = lists[0]
        i = 1
        while(i < n):
            result = self.merge(result, lists[i])
            i += 1
        return result

    