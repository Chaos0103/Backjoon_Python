def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

computer = int(input())
link = int(input())
graph = [[] for _ in range(computer+1)]
visited = [False] * (computer + 1)
for _ in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
cnt = visited.count(True)
print(cnt-1)
