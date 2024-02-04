from collections import deque

class Node:
    def __init__(self, node_id: str) -> None:
        self.id: str = node_id
        self.neighbors: set[str] = set()
    
    def add_edge_to(self, node_id: str) -> None:
        self.neighbors.add(node_id)
    
    def has_edge_to(self, node_id: str) -> bool:
        return node_id in self.neighbors

class Graph:
    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}

    def get_or_make_node(self, node_id: str) -> Node:
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)
        return self.nodes[node_id]
    
    def add_edge(self, source_id: str, destination_id: str) -> None:
        source = self.get_or_make_node(source_id)
        source.add_edge_to(destination_id)
        

    def has_edge(self, source_id: str, destination_id: str) -> bool:
        source = self.get_or_make_node(source_id)
        return source.has_edge_to(destination_id)
    
    def search_by_dfs(self, source_id: str, destination_id: str) -> bool:
        return self.search_by_dfs_helper(source_id, destination_id, set())

    def search_by_dfs_helper(self, source_id: str, destination_id: str, visited: set[str]) -> bool:
        print(f"Current {source_id} | nodes visited so far : {visited}")
        if source_id==destination_id:
            return True
        else:
            source = self.get_or_make_node(source_id)
            visited.add(source_id)
            
            for neighbor_id in source.neighbors:
                if neighbor_id not in visited:
                    return self.search_by_dfs_helper(neighbor_id, destination, visited)
        return False
    
    def search_by_bfs(self, source_id: str, destination_id: str) -> bool:
        queue = deque()
        queue.appendleft(source_id)
        visited = set()
        while queue:
            node_id = queue.pop()
            print(f"Current {node_id} | nodes visited so far : {visited}")
            if node_id==destination_id:
                return True
            visited.add(node_id)
            node = self.get_or_make_node(node_id)
            for neighbor_id in node.neighbors:
                if neighbor_id not in visited:
                    queue.appendleft(neighbor_id)
        return False
        
if __name__=="__main__":
    graph = Graph()
    edges = [("a", "b"), ("a", "d"), \
            ("b", "c"), ("b", "e"), \
            ("d", "c"), \
            ("c", "g"), ("c", "f"), \
            ("e", "h"), \
            ("g", "f"), \
            ("f", "h")]

    for (source, destination) in edges:
        print(f"Adding {source} -> {destination} edge")
        graph.add_edge(source, destination)

    def has_a_direct_edge(graph: Graph, source_id: str, destination_id: str) -> None:
        print(f"Is edge {source_id}->{destination_id} exists ? : {graph.has_edge(source_id, destination_id)}")

    def has_a_path_dfs(graph: Graph, source_id: str, destination_id: str) -> None:
        print(f"[DFS] Is a path between {source_id} and {destination_id} exists ? : {graph.search_by_dfs(source_id, destination_id)}")

    def has_a_path_bfs(graph: Graph, source_id: str, destination_id: str) -> None:
        print(f"[BFS] Is a path between {source_id} and {destination_id} exists ? : {graph.search_by_bfs(source_id, destination_id)}")

    has_a_direct_edge(graph, "a", "h")
    has_a_path_dfs(graph, "a", "h")
    has_a_path_bfs(graph, "a", "h")
        