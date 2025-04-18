import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from johnson_algorithm import johnson, INF

def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        graph = []
        for line in lines:
            row = [float(x) if x != 'INF' else INF for x in line.strip().split()]
            graph.append(row)
    return graph

def visualize_graph(graph, path_matrix, start, end):
    G = nx.DiGraph()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != INF:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path_matrix and path_matrix[start][end] != INF:
        path_edges = [(start, end)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Визуализация графа (Johnson)")
    plt.show()

def main():
    graph = read_graph_from_file("johnson_graph.txt")

    def on_run():
        try:
            start = int(entry_start.get())
            end = int(entry_end.get())
            if start < 0 or end >= len(graph):
                raise ValueError

            result = johnson(graph)
            if result is None:
                messagebox.showerror("Ошибка", "Обнаружен отрицательный цикл.")
                return

            distance = result[start][end]
            if distance == INF:
                messagebox.showinfo("Результат", f"Нет пути от {start} до {end}")
            else:
                messagebox.showinfo("Результат", f"Кратчайшее расстояние от {start} до {end}: {distance}")
                visualize_graph(graph, result, start, end)
        except:
            messagebox.showerror("Ошибка", "Некорректный ввод")

    root = tk.Tk()
    root.title("Алгоритм Джонсона")

    tk.Label(root, text="Начальная вершина:").pack()
    entry_start = tk.Entry(root)
    entry_start.pack()

    tk.Label(root, text="Конечная вершина:").pack()
    entry_end = tk.Entry(root)
    entry_end.pack()

    tk.Button(root, text="Вычислить", command=on_run).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
