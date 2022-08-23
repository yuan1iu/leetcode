# 146. LRU Cache
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.count = 0
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.count -= 1
        
        
    def insert_node(self, node):
        node.next = self.left.next
        self.left.next.prev = node
        self.left.next = node
        node.prev = self.left
        self.count += 1
        
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove_node(self.cache[key])
        self.insert_node(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # update the value if it exists
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])
        if self.count > self.capacity:
            del self.cache[self.right.prev.key]
            self.remove_node(self.right.prev)
