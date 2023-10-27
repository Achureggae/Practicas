class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self, max_cost=False):
        self.edges.sort(key=lambda x: x[2], reverse=max_cost)
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        mst = []

        for edge in self.edges:
            u, v, weight = edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                mst.append(edge)
                self.union(parent, rank, x, y)

        return mst


g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst = g.kruskal_mst(max_cost=False) 
print("Árbol de Mínimo Costo:")
for u, v, w in mst:
    print(f"Arista ({u}-{v}) Peso: {w}")

mst = g.kruskal_mst(max_cost=True)  
print("\nÁrbol de Máximo Costo:")
for u, v, w in mst:
    print(f"Arista ({u}-{v}) Peso: {w}")
