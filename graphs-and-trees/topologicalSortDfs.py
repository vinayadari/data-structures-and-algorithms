from collections import defaultdict
def topo_sort_dfs(V, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    visited = set()
    order = []
    def dfs(v):
        visited.add(v)
        for nei in graph[v]:
            if nei not in visited:
                dfs(nei)
        order.append(v)
    for v in range(1,V+1):
        if v not in visited:
            dfs(v)
    return order[::-1]
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))
edges = []
print("Enter edges (u v) one per line:")
for _ in range(E):  
    u, v = map(int, input().split())
    edges.append((u, v))
result = topo_sort_dfs(V, edges)
print("Topological Sort Order:", result)
