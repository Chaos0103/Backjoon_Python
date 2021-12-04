n, m = map(int, input().split())
x, y, d = map(int, input().split())

visited = [[0]*m for _ in range(n)]
visited[x][y] = 1

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

def turn():
    global d
    d -= 1
    if d == -1:
        d = 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
cnt = 1
while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and data[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        time = 0
        continue
    else:
        time += 1

    if time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        time = 0

print(cnt)
