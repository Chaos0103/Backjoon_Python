from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())

data = deque()

for i in range(1, N+1):
    data.append(i)

print('<', end='')
while len(data) != 1:
    for _ in range(M-1):
        data.append(data[0])
        data.popleft()
    print(data[0], end=', ')
    data.popleft()
print(data[0], end='')
print('>')

# queue
