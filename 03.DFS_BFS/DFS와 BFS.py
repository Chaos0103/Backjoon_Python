from collections import deque

N, M, V = map(int, input().split())
data = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    data[x][y] = y
    data[y][x] = x

result = [False] * 1001


def dfs(arr, result, start):
    result[start] = True
    print(start, end=' ')
    for i in arr[start]:
        if i == 0:
            continue
        if not(result[i]):
            dfs(arr, result, i)


bresult = [False] * 1001

def bfs(arr, bresult, start):
    queue = deque([start])
    bresult[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in arr[v]:
            if i == 0:
                continue
            if not(bresult[i]):
                queue.append(i)
                bresult[i] = True


dfs(data, result, V)
print()
bfs(data, bresult, V)
