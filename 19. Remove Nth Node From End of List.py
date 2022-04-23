# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = ListNode(0)
        dummy = cur
        cur.next = head
        while head:
            count += 1
            head = head.next

        idx = count - n
        while idx > 0:
            idx -= 1
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
