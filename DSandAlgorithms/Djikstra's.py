def Djikstra(installation_A, installation_B, graph):
    visited = []
    unvisited = []
    distances = []
    previous = []
    name2idx = graph.artwork_to_index
    current = name2idx[installation_A] ## start node
    count = name2idx[installation_B] ## end node
    for i in range(len(graph.adjacency_mtx)):
        distances.append(float('inf')) ## initialize all distances to infinity
    distances[current] = 0
    for i in range(len(graph.adjacency_mtx)):
        previous.append(-1) ## impossible distance for reference
    for i in graph.installations:
        unvisited.append(name2idx[i]) ## change string to indexes
    while unvisited != [] and current in unvisited:
        min_distance = float("inf")
        visited.append(current)
        unvisited.remove(current)
        for i in unvisited:
            if graph.adjacency_mtx[current][i] != 0 and distances[current] + graph.adjacency_mtx[current][i] < distances[i]:
                distances[i] = distances[current] + graph.adjacency_mtx[current][i]
                previous[i] = current ## update
        for i in unvisited:
            if distances[i] < min_distance:
                min_node = i
                min_distance = distances[i]
        current = min_node
    if previous[count] == -1:
        return (None, [])
    else:
        path = [graph.installations[count]]
        end = count
        while previous[end] != -1:
            end = previous[end]
            path.append(graph.installations[end])
        path.reverse()
        return (distances[count], path)