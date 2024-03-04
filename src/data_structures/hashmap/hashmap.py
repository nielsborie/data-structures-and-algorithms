class ListNode:
    def __init__(self, key: int = -1, val: int = -1, next: 'ListNode' = None) -> None:
        self.val = val
        self.key = key
        self.next = next


class HashMap:
    def __init__(self, MAX_SIZE: int = 1000) -> None:
        self.map: list[ListNode] = [ListNode() for _ in range(MAX_SIZE)]

    def hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def delete(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        return not self.get(key) == -1

    def get_size(self) -> int:
        pass
