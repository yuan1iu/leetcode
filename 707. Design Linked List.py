# 707. Design Linked List
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0      

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)       

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        # make cur pointing to the head
        cur = self.head
        new = ListNode(val)
        if index == 0:
            new.next = self.head
            self.head = new
        else:
            while index - 1> 0:
                cur = cur.next
                index -= 1
            new.next = cur.next
            cur.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        cur = self.head
        
        if index == 0:
            self.head = cur.next
        else:
            while index-1 > 0:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
        self.size -= 1


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0      

    def get(self, index: int) -> int:
        if index >= self.size: return -1     
        return self.getNode(index).val

    def getNode(self, index: int) -> int:
        if index < self.size // 2:
            cur = self.head
            while index > 0:
                cur = cur.next
                index -= 1           
        else:
            cur = self.tail
            while index < self.size - 1:
                cur = cur.prev
                index += 1
        return cur

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        if self.size == 0:
            self.tail = new
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if self.size == 0:
            self.tail = new
            self.head = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            
        elif index == self.size:
            self.addAtTail(val)

        else:
            node = self.getNode(index)
            new = ListNode(val)
            new.prev = node.prev
            new.next = node
            node.prev.next = new
            node.prev = new
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        
        if index == 0 and self.size == 1:
            self.head, self.tail = None, None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1: # delete tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self.getNode(index)
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

class ListNode():
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None
