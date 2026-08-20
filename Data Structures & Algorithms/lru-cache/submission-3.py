from collections import deque

class Node:
    def __init__(self, key: int = -1, val: int = 0, prev: Node = None, next: Node = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.items = dict()
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
    
    def remove(node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next, next_node.prev = next_node, prev_node
        node.prev, node.next = None, None
    
    def insert(self, insert_node: Node) -> None:
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = insert_node
        insert_node.next, insert_node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.items:
            cached_node = self.items[key]
            LRUCache.remove(cached_node)
            self.insert(cached_node)
            return self.items[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            cached_node = self.items[key]
            cached_node.val = value
            LRUCache.remove(cached_node)
            self.insert(cached_node)
            return
        self.items[key] = Node(key=key, val=value)
        latest_node = self.tail.prev
        self.insert(self.items[key])
        if len(self.items) > self.capacity:
            lru_node = self.head.next
            del self.items[lru_node.key]
            LRUCache.remove(lru_node)





        
