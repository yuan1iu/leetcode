

for i in range(5 - 1, -1):
    print(i)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry == 1:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_node = ListNode((l1_val + l2_val + carry) % 10)
            carry = 1 if l1_val + l2_val + carry > 9 else 0
            cur.next = new_node
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
