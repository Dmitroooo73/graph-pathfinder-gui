import time
import numpy as np
from yen_algorithm import yen_k_shortest_paths, INF

def generate_graph(V):
    np.random.seed(0)
    graph = np.random.randint(1, 10, size=(V, V)).astype(float)
    graph[graph > 7] = INF
    np.fill_diagonal(graph, 0)
    return graph

def analyze_time():
    print("\nАнализ времени выполнения алгоритма Йена:")
    for V in [5, 10, 15]:
        graph = generate_graph(V)
        start_time = time.time()
        paths = yen_k_shortest_paths(graph, 0, V - 1, 3)
        elapsed_time = time.time() - start_time
        print(f"Вершины: {V}, Время выполнения: {elapsed_time:.6f} сек, Найдено путей: {len(paths)}")

if __name__ == "__main__":
    analyze_time()


