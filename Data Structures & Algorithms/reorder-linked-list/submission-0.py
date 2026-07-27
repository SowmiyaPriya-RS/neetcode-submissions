# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while(fast.next):
            slow = slow.next
            fast = fast.next
            if(fast.next):
                fast = fast.next

        prev = None
        curr = slow.next
        slow.next = None
        while(curr):
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n

        first = head
        second = prev
        while(second):
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2

            
        


