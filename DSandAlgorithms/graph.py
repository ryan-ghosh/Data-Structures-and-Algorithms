# adj list representation

class Node:
    def __init__(self, value):
        self.value = value
        self.adj_list = list()

    def __repr__(self):
        return str(self.value)

    def add_neighbour(self, v):
        if v not in self.adj_list:
            self.adj_list.append(v)
            self.adj_list.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if vertex.value not in self.vertices:
            self.vertices[vertex.value] = vertex

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbour(v)
            self.vertices[v].add_neighbour(u)

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, ":", str(self.vertices[key].adj_list))


if __name__ == "__main__":
    g = Graph()
    a = Node('A')
    g.add_vertex(a)
    g.add_vertex(Node('B'))
    for i in range(ord('A'), ord('K')):
        g.add_vertex(Node(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])

    g.print_graph()
