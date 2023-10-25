class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start_node):
        visited = set()

        def dfs_recursive(node):
            if node not in visited:
                print(node, end=" ")  # Visit the current node
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)

# Example usage
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("Depth-First Traversal starting from node 2:")
graph.dfs(2)
