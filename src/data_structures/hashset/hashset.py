class ListNode:
    def __init__(self, key: int = -1) -> None:
        self.key = key
        self.next = None


class HashSet:
    def __init__(self) -> None:
        self.MAX_SIZE = 10 ** 4
        self.set = [ListNode() for _ in range(self.MAX_SIZE)]

    def add(self, key: int) -> None:
        idx = key % len(self.set)
        cur = self.set[idx]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % len(self.set)
        cur = self.set[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        idx = key % len(self.set)
        cur = self.set[idx]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False
