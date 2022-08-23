class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        nxt = (self.rear+1) % self.capacity
        self.rear = nxt
        self.queue[nxt] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:  # only one item
            self.rear = -1
            self.front = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear+1) % self.capacity == self.front:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(2)
obj.enQueue(1)
obj.enQueue(2)
obj.deQueue()
obj.enQueue(3)
obj.deQueue()
obj.enQueue(3)
obj.deQueue()
obj.enQueue(3)
obj.deQueue()
obj.Front()
