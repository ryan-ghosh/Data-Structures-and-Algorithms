import random

class Vertex:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Graph:
    def __init__(self, vertexList=[], adj_mtx=[]):
        self.vertexList = vertexList
        self.adj_mtx = adj_mtx

    def add_vertex(self, v: Vertex):
        """
        :param v: vertex
        :param neighbours: vertex with associated weight
        :return: None
        """
        self.vertexList.append(v)
        self.adj_mtx.append([])
        for i in range(len(self.vertexList)):
            if i != len(self.vertexList)-1:
                self.adj_mtx[i].append(0)
            elif i == len(self.vertexList)-1:
                for j in range(len(self.vertexList)):
                    self.adj_mtx[len(self.vertexList)-1].append(0)

    def add_edge(self, node1: Vertex, node2: Vertex, weight: int):
        if node1 not in self.vertexList:
            self.add_vertex(node1)
        if node2 not in self.vertexList:
            self.add_vertex(node2)
        index1 = self.vertexList.index(node1)
        index2 = self.vertexList.index(node2)
        self.adj_mtx[index1][index2] = weight
        self.adj_mtx[index2][index1] = weight
        return 1

    def Djikstra(self, start, end):
        visited = []
        unvisited = []
        distances = []
        previous = []
        current = self.vertexList.index(start)  ## start node
        count = self.vertexList.index(end)  ## end node
        for i in range(len(self.adj_mtx)):
            distances.append(float('inf'))  ## initialize all distances to infinity
        distances[current] = 0
        for i in range(len(self.adj_mtx)):
            previous.append(-1)  ## impossible distance for reference
        for i in self.vertexList:
            unvisited.append(self.vertexList.index(i))  ## change to indexes

        while unvisited != [] and current in unvisited:
            min_distance = float("inf")
            visited.append(current)
            unvisited.remove(current)
            for i in unvisited:
                if self.adj_mtx[current][i] != 0 and distances[current] + self.adj_mtx[current][i] < \
                        distances[i]:
                    distances[i] = distances[current] + self.adj_mtx[current][i]
                    previous[i] = current  ## update
            for i in unvisited:
                if distances[i] < min_distance:
                    min_node = i
                    min_distance = distances[i]
            current = min_node
        if previous[count] == -1:
            return None, []
        else:
            path = [self.vertexList[count]]
            end = count
            while previous[end] != -1:
                end = previous[end]
                path.append(self.vertexList[end])
            path.reverse()
            return distances[count], path

    def AStar(self, start, end):
        pass


if __name__ == "__main__":
    G = Graph()
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')
    j = Vertex('j')
    k = Vertex('k')
    l = Vertex('l')
    m = Vertex('m')

    G.add_vertex(a)
    G.add_vertex(b)
    G.add_vertex(c)
    G.add_vertex(d)
    G.add_vertex(e)
    G.add_vertex(f)
    G.add_vertex(g)
    G.add_vertex(h)
    G.add_vertex(i)
    G.add_vertex(j)
    G.add_vertex(k)
    G.add_vertex(l)
    G.add_vertex(m)

    G.add_edge(c, b, 10)
    G.add_edge(c, e, 5)
    G.add_edge(e, a, 6)
    G.add_edge(e, m, 8)
    G.add_edge(e, h, 3)
    G.add_edge(a, b, 26)
    G.add_edge(a, d, 8)
    G.add_edge(c, f, 15)
    G.add_edge(h, i, 7)
    G.add_edge(h, l, 10)
    G.add_edge(h, j, 5)
    G.add_edge(l, g, 11)
    G.add_edge(i, g, 3)
    G.add_edge(i, m, 1)
    G.add_edge(b, k, 14)
    G.add_edge(f, k, 4)
    G.add_edge(d, f, 8)
    G.add_edge(g, j, 9)
    print(G.Djikstra(j, b))







