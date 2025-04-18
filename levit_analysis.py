import time
import numpy as np
from levit_algorithm import levit, INF

def generate_graph(V):
    np.random.seed(0)
    graph = np.random.randint(1, 10, size=(V, V)).astype(float)
    graph[graph > 7] = INF
    np.fill_diagonal(graph, 0)
    return graph

def analyze_time():
    print("\nАнализ времени выполнения алгоритма Левита:")
    print(f"{'Вершины':<10} {'Рёбра':<10} {'Время (сек)':<15}")
    print("-" * 35)
    for V in [5, 10, 20, 50]:
        graph = generate_graph(V)
        E = sum(1 for i in range(V) for j in range(V) if graph[i][j] != INF and i != j)
        start_time = time.time()
        levit(graph, 0, V - 1)
        elapsed_time = time.time() - start_time
        print(f"{V:<10} {E:<10} {elapsed_time:<15.6f}")

if __name__ == "__main__":
    analyze_time()
