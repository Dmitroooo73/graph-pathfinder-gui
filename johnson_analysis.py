import time
import numpy as np
from johnson_algorithm import johnson, INF

def generate_graph(V):
    np.random.seed(0)
    graph = np.random.randint(-3, 10, size=(V, V)).astype(float)
    graph[graph > 7] = INF
    np.fill_diagonal(graph, 0)
    return graph

def analyze_time():
    print("\nАнализ времени выполнения (Johnson):")
    for V in [5, 10, 20, 30]:
        graph = generate_graph(V)
        start = time.time()
        result = johnson(graph)
        elapsed = time.time() - start
        print(f"Вершины: {V}, Время выполнения: {elapsed:.6f} сек")

if __name__ == "__main__":
    analyze_time()
