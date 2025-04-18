from collections import deque

INF = float('inf')

def levit(graph, start, end):
    V = len(graph)
    M0, M1, M2 = set(), set(range(V)), set()
    distance = [INF] * V
    prev = [None] * V
    queue = deque()

    distance[start] = 0
    queue.append(start)
    M1.remove(start)
    M0.add(start)

    while queue:
        u = queue.popleft()
        for v in range(V):
            if graph[u][v] == INF or u == v:
                continue

            new_dist = distance[u] + graph[u][v]
            if v in M2:
                if new_dist < distance[v]:
                    distance[v] = new_dist
                    prev[v] = u
                    M2.remove(v)
                    queue.appendleft(v)
                    M0.add(v)
            elif v in M1:
                distance[v] = new_dist
                prev[v] = u
                queue.append(v)
                M1.remove(v)
                M0.add(v)
            elif v in M0 and new_dist < distance[v]:
                distance[v] = new_dist
                prev[v] = u

        M0.remove(u)
        M2.add(u)

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()

    return distance[end], path

