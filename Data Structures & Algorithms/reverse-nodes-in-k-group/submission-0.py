# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getkth(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        while(curr and k>0):
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grp_prev = dummy

        while True:
            kth = self.getkth(grp_prev, k)
            if not kth:
                break
            grp_next = kth.next
            
            prev = kth.next
            curr = grp_prev.next
            while(curr != grp_next):
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            
            tmp = grp_prev.next
            grp_prev.next = kth
            grp_prev = tmp

        return dummy.next