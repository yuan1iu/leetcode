# 708. Insert into a Sorted Circular Linked List
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new = ListNode(insertVal)
        if not head:
            new.next = new
            return new
        
        prev, succ = head, head.next
        while True:
            if insertVal >= prev.val and insertVal <= succ.val:                
                break
            if prev.val > succ.val and (insertVal >= prev.val or insertVal <= succ.val):
                break
            
            prev, succ = prev.next, succ.next
            
            # move next before case 3->3->3, make sure prev pointer will move a whole round
            if prev == head:
                break
            
        prev.next = new
        new.next = succ
        return head