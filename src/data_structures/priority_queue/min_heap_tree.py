class HeapNode:
    def __init__(self, value: int):
        self.left: HeapNode = None
        self.right: HeapNode = None
        self.data: int = value


class MinHeap:
    def __init__(self):
        self.root: HeapNode = None

    def insert(self, value: int) -> None:
        """
        Insert a new value in the min heap and still preserve the consistency in the structure (ie every child nodes need to be higher than parent nodes)

        Args:
            value (int): the value to insert in the min heap

        Returns:
            HeapNode: the root HeapNode of the MinHeap after heapify
        """
        if not self.root:
            self.root = HeapNode(value)
        else:
            self._insert_recursive(self.root, value)
            self._heapify_up()

    def _insert_recursive(self, current, value):
        if not current.left:
            current.left = HeapNode(value)
        elif not current.right:
            current.right = HeapNode(value)
        else:
            # Insert in a balanced manner
            self._insert_recursive(current.left, value)

            # After insertion, check if the left child's value is smaller than the current node
            if current.left.data < current.data:
                # Swap values if necessary
                current.data, current.left.data = current.left.data, current.data

            # Note: No need to check the right child in this case

    def extract_min(self) -> int:
        """
        Get the top of the heap; the minium value in the data structure.
        Returns:
            int: top of the min heap
        """
        if not self.root:
            return None

        min_value = self.root.data

        # Replace the root with the last inserted node
        last_node_value = self._remove_last_node()
        self.root.data = last_node_value

        self._heapify_down()

        return min_value

    def _remove_last_node(self) -> int:
        last_node_value = None

        if self.root:
            queue = [self.root]
            last_node = None

            while queue:
                current = queue.pop(0)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

                last_node = current

            if last_node.left:
                last_node_value = last_node.left.data
                last_node.left = None
            elif last_node.right:
                last_node_value = last_node.right.data
                last_node.right = None
            else:
                # If there is only one node in the tree
                last_node_value = last_node.data

                # Update parent's reference
                parent = self._find_parent_of_last_node()
                if parent:
                    if parent.left == last_node:
                        parent.left = None
                    elif parent.right == last_node:
                        parent.right = None
                    else:
                        last_node_value = parent.data
                        self.root = None
                    # Note: No need to update parent's reference if last_node is the root

            return last_node_value

    def _find_parent_of_last_node(self) -> HeapNode | None:
        if not self.root:
            return None

        queue = [self.root]
        parent = None

        while queue:
            current = queue.pop(0)

            if current.left:
                queue.append(current.left)
                parent = current
            if current.right:
                queue.append(current.right)
                parent = current

        return parent

    def _get_height(self, node: HeapNode) -> int:
        if not node:
            return 0
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return 1 + max(left_height, right_height)

    def _heapify_up(self):
        current = self.root

        while current:
            if current.left and current.left.data < current.data:
                current.data, current.left.data = current.left.data, current.data
                current = current.left
            elif current.right and current.right.data < current.data:
                current.data, current.right.data = current.right.data, current.data
                current = current.right
            else:
                break

    def _heapify_down(self):
        current = self.root

        while current:
            min_node = current
            if current.left and current.left.data < min_node.data:
                min_node = current.left
            if current.right and current.right.data < min_node.data:
                min_node = current.right

            if min_node != current:
                current.data, min_node.data = min_node.data, current.data
                current = min_node
            else:
                break


if __name__ == "__main__":
    # Exemple d'utilisation
    min_heap = MinHeap()
    min_heap.insert(4)
    min_heap.insert(2)
    min_heap.insert(8)
    min_heap.insert(1)
    print(f"Peek the minimum value in the MinHeap : {min_heap.root.data=}")
    print(f"- Extracting minimum value from the MinHeap ...")
    minimum = min_heap.extract_min()
    print(f"Minimum value extracted : {minimum=}")
    print(f"Peek the minimum value in the MinHeap : {min_heap.root.data=}")
