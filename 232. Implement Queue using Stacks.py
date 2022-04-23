# 232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.enque_stack = []
        self.deque_stack = []

    def push(self, x: int) -> None:
        self.enque_stack.append(x)

    def pop(self) -> int:
        if len(self.deque_stack) == 0:  # only when enque_stack has items
            while len(self.enque_stack) > 0:
                self.deque_stack.append(self.enque_stack.pop())
        return self.deque_stack.pop()

    def peek(self) -> int:
        if len(self.deque_stack) == 0:
            while len(self.enque_stack) > 0:
                self.deque_stack.append(self.enque_stack.pop())
        return self.deque_stack[-1]

    def empty(self) -> bool:
        if len(self.enque_stack) == 0 and len(self.deque_stack) == 0:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
