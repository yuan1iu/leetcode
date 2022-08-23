# 24. Swap Nodes in Pairs
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next: return head
        cur = head.next
        next = head.next.next
        head.next.next = head
        head.next = self.swapPairs(next)
        return cur
        