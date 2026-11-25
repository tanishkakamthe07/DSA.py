class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        if 0 <= u < self.V and 0 <= v < self.V:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # Undirected graph

    def display_matrix(self):
        print("\n--- Adjacency Matrix ---")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = [False] * self.V

        visited[start_vertex] = True
        print(start_vertex, end=" ")

        for neighbor in range(self.V):
            if self.adj_matrix[start_vertex][neighbor] == 1 and not visited[neighbor]:
                self.dfs(neighbor, visited)


if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    g = Graph(v)

    print("Enter edges (u v) using 0-based indexing:")
    for _ in range(e):
        u, w = map(int, input().split())
        g.add_edge(u, w)

    g.display_matrix()

    start = int(input("\nEnter starting vertex for DFS: "))
    if 0 <= start < v:
        print("DFS Traversal: ", end="")
        g.dfs(start)
        print()
    else:
        print("Invalid starting vertex.")
