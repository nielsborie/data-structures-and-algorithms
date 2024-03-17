class ListNode:
    def __init__(self, key: int = -1, val: int = -1) -> None:
        self.val = val
        self.key = key
        self.next = None

class HashMap:
    def __init__(self, MAX_SIZE: int = 1000) -> None:
        self.MAX_SIZE = MAX_SIZE
        self.hashmap: list[ListNode] = [ListNode() for _ in range(self.MAX_SIZE)]

    def hash(self, key: int) -> int:
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        cur = self.hashmap[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.hashmap[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def delete(self, key: int) -> None:
        idx = self.hash(key)
        cur = self.hashmap[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        return not self.get(key) == -1

    def get_size(self) -> int:
        size = 0
        for node in self.hashmap:
            while node.next:
                size += 1
                node = node.next
        return size
