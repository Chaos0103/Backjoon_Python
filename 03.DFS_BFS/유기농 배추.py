import sys
# 재귀 깊이 증가
sys.setrecursionlimit(10**6)

case = int(input())


def dfs(X, Y):
    if X < 0 or Y < 0 or X >= M or Y >= N:
        return False
    if data[X][Y] == 1:
        data[X][Y] = 0
        dfs(X+1, Y)
        dfs(X-1, Y)
        dfs(X, Y+1)
        dfs(X, Y-1)
        return True
    return False


for _ in range(case):
    M, N, K = map(int, input().split())
    data = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        data[x][y] = 1
    result = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                result += 1

    print(result)
