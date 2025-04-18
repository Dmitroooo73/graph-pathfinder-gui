from levit_algorithm import levit, INF

def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    graph = []
    for line in lines:
        row = [float(x) if x != 'INF' else INF for x in line.strip().split()]
        graph.append(row)
    return graph

if __name__ == "__main__":
    graph = read_graph_from_file("levit_graph.txt")
    start, end = 0, 4
    dist, path = levit(graph, start, end)
    print(f"Расстояние от {start} до {end}: {dist}")
    print("Путь:", ' → '.join(map(str, path)))
