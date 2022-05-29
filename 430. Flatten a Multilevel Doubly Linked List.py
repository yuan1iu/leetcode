# 430. Flatten a Multilevel Doubly Linked List
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    def dfs(cur):
        if (cur.child is not None):
            tail = dfs(cur.child)
            tail.next = cur.next
            if (cur.next is not None):
                cur.next.prev = tail
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
            if (tail.next is None): 
                return tail
            a = dfs(tail.next)
            return a
        
        if (cur.next is None):
            return cur;
        s = dfs(cur.next)
        return s
    
    head = dfs(head)
    return head


def flatten2(head):
    
    def dfs(node):
        if not node: return None
        if not node.child:
            if not node.next: return node
            level_tail = dfs(node.next)
            return level_tail
            
        else:
            tail = dfs(node.child)
            next = node.next
            node.next = node.child                
            node.child.prev = node
            node.child = None
            tail.next = next
            if next:
                next.prev = tail
                s = dfs(next)
                return s
            return tail

    dfs(head)
    return head

def flatten3(head):
    def dfs(cur):
        nxt = cur.next
        if cur.child:            
            child_tail = dfs(cur.child)
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
            if nxt:
                next_tail = dfs(nxt)
                child_tail.next = nxt
                nxt.prev = child_tail
                return next_tail
            return child_tail
        else:
            if nxt:
                return dfs(nxt)
            else:
                return cur
    if not head: return None
    s = dfs(head)




obj1= Node(1, None, None, None)
obj2= Node(2,obj1, None, None)
obj3= Node(3,None, None, None)
obj4 = Node(4,obj3,None,None)
obj5 = Node(5,obj4,None,None)
obj6 = Node(6,None,None,None)

obj3.next=obj4
obj1.child = obj3
obj3.child=obj6
obj1.next = obj2
obj4.next=obj5
flatten3(obj1)

