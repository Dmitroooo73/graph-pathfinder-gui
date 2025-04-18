import heapq

INF = float('inf')

def dijkstra(graph, start, end):
    V = len(graph)
    distances = [INF] * V
    previous = [None] * V
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        dist_u, u = heapq.heappop(queue)

        if u == end:
            break

        for v, weight in enumerate(graph[u]):
            if weight != INF:
                alt = dist_u + weight
                if alt < distances[v]:
                    distances[v] = alt
                    previous[v] = u
                    heapq.heappush(queue, (alt, v))

    path = []
    current = end
    if distances[end] == INF:
        return INF, []

    while current is not None:
        path.append(current)
        current = previous[current]
    return distances[end], path[::-1]

def yen_k_shortest_paths(graph, start, end, K):
    distance, path = dijkstra(graph, start, end)
    if distance == INF:
        return []

    paths = [(distance, path)]
    potential_paths = []

    for k in range(1, K):
        for i in range(len(paths[-1][1]) - 1):
            spur_node = paths[-1][1][i]
            root_path = paths[-1][1][:i + 1]

            temp_graph = [row[:] for row in graph]

            for cost, p in paths:
                if p[:i + 1] == root_path and len(p) > i + 1:
                    u, v = p[i], p[i + 1]
                    temp_graph[u][v] = INF

            for node in root_path[:-1]:
                temp_graph[node] = [INF] * len(graph)

            spur_dist, spur_path = dijkstra(temp_graph, spur_node, end)
            if spur_dist != INF:
                total_path = root_path[:-1] + spur_path
                total_dist = sum(graph[total_path[i]][total_path[i + 1]] for i in range(len(total_path) - 1))
                if (total_dist, total_path) not in potential_paths:
                    heapq.heappush(potential_paths, (total_dist, total_path))

        if not potential_paths:
            break

        paths.append(heapq.heappop(potential_paths))

    return paths
