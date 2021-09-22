from collections import deque
import sys
N = int(sys.stdin.readline())

data = deque()

for i in range(1, N+1):
    data.append(i)

while len(data) != 1:
    data.popleft()
    data.append(data[0])
    data.popleft()

print(data[0])

# queue
