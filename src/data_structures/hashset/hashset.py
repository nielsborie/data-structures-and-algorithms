class ListNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.next = None
        
class HashSet:
    def __init__(self) -> None:
        MAX_SIZE = 10**4
        self.set = [ListNode(0) for _ in range(MAX_SIZE)]
    
    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
    
    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
            cur = cur.next
    
    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False