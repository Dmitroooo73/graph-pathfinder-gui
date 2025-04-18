import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import networkx as nx
from levit_algorithm import levit, INF

def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    graph = []
    for line in lines:
        row = [float(x) if x != 'INF' else INF for x in line.strip().split()]
        graph.append(row)
    return graph

def visualize_graph(graph, path):
    G = nx.DiGraph()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != INF and i != j:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)
    edge_labels = {(i, j): graph[i][j] for i, j in G.edges()}
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    if path and len(path) > 1:
        nx.draw_networkx_edges(G, pos, edgelist=list(zip(path, path[1:])), edge_color='red', width=2)

    plt.title("Граф и кратчайший путь (Левит)")
    plt.show()

def main():
    def load_file():
        nonlocal graph, V
        filename = filedialog.askopenfilename()
        graph = read_graph_from_file(filename)
        if graph:
            V = len(graph)
            messagebox.showinfo("Граф загружен", "Граф успешно загружен!")

    def find_path():
        try:
            start = int(entry_start.get())
            end = int(entry_end.get())
            if start >= V or end >= V or start < 0 or end < 0:
                raise ValueError("Некорректные номера вершин")
            dist, path = levit(graph, start, end)
            result_text.set(f"Кратчайшее расстояние: {dist}\nПуть: {' → '.join(map(str, path))}")
            visualize_graph(graph, path)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    root = tk.Tk()
    root.title("Алгоритм Левита")

    graph = []
    V = 0

    tk.Button(root, text="Загрузить граф из файла", command=load_file).pack()
    tk.Label(root, text="Начальная вершина:").pack()
    entry_start = tk.Entry(root)
    entry_start.pack()
    tk.Label(root, text="Конечная вершина:").pack()
    entry_end = tk.Entry(root)
    entry_end.pack()
    tk.Button(root, text="Найти кратчайший путь", command=find_path).pack()
    result_text = tk.StringVar()
    tk.Label(root, textvariable=result_text).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
