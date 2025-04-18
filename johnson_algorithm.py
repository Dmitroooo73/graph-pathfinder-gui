import heapq

INF = float('inf')

def bellman_ford(graph, V, start):
    distances = [INF] * V
    distances[start] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                if graph[u][v] != INF and distances[u] != INF:
                    if distances[u] + graph[u][v] < distances[v]:
                        distances[v] = distances[u] + graph[u][v]

    for u in range(V):
        for v in range(V):
            if graph[u][v] != INF and distances[u] + graph[u][v] < distances[v]:
                return None  # Обнаружен отрицательный цикл

    return distances

def dijkstra(graph, start):
    V = len(graph)
    distances = [INF] * V
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        for v, weight in enumerate(graph[u]):
            if weight != INF:
                new_dist = current_dist + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

    return distances

def johnson(graph):
    V = len(graph)

    # Правильно расширяем матрицу
    extended_graph = [row + [0] for row in graph]
    extended_graph.append([0] * (V + 1))

    h = bellman_ford(extended_graph, V + 1, V)
    if h is None:
        return None  # отрицательный цикл

    reweighted = [[INF] * V for _ in range(V)]
    for u in range(V):
        for v in range(V):
            if graph[u][v] != INF:
                reweighted[u][v] = graph[u][v] + h[u] - h[v]

    all_pairs = []
    for u in range(V):
        d = dijkstra(reweighted, u)
        corrected = [d[v] + h[v] - h[u] if d[v] != INF else INF for v in range(V)]
        all_pairs.append(corrected)

    return all_pairs

