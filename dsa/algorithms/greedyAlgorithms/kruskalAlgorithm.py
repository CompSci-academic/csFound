class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        mst = []
        num_edges = 0
        index = 0

        while num_edges < self.V - 1:
            u, v, w = self.graph[index]
            index += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append([u, v, w])
                self.union(parent, x, y)
                num_edges += 1

        # Print the Minimum Spanning Tree
        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} - {v}, Weight: {weight}")

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set

# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal()
