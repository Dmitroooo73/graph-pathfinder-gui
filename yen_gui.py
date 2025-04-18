import tkinter as tk
from tkinter import filedialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from yen_algorithm import yen_k_shortest_paths, INF

def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        graph = []
        for line in lines:
            row = [float(x) if x != 'INF' else INF for x in line.strip().split()]
            graph.append(row)
    return graph

def visualize_graph(graph, paths=None):
    G = nx.DiGraph()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != INF:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)})

    if paths:
        for path in paths:
            edges = list(zip(path[1][:-1], path[1][1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)

    plt.show()

def main():
    graph = read_graph_from_file("yen_graph.txt")

    def on_calculate():
        try:
            start = int(entry_start.get())
            end = int(entry_end.get())
            k = int(entry_k.get())
            if start < 0 or end >= len(graph) or k <= 0:
                raise ValueError
            paths = yen_k_shortest_paths(graph, start, end, k)
            if not paths:
                messagebox.showinfo("Результат", "Пути не найдены.")
            else:
                result_text = "\n".join([f"{i + 1}) Длина: {p[0]}, Путь: {p[1]}" for i, p in enumerate(paths)])
                messagebox.showinfo("Результат", result_text)
                visualize_graph(graph, paths)
        except:
            messagebox.showerror("Ошибка", "Неверный ввод или невозможный путь.")

    root = tk.Tk()
    root.title("Алгоритм Йена")
    tk.Label(root, text="Стартовая вершина:").pack()
    entry_start = tk.Entry(root)
    entry_start.pack()
    tk.Label(root, text="Конечная вершина:").pack()
    entry_end = tk.Entry(root)
    entry_end.pack()
    tk.Label(root, text="Количество путей (K):").pack()
    entry_k = tk.Entry(root)
    entry_k.pack()
    tk.Button(root, text="Вычислить", command=on_calculate).pack()
    root.mainloop()

if __name__ == "__main__":
    main()
